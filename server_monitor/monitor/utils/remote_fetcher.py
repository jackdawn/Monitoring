import paramiko
import winrm

def fetch_linux_metrics(server):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server.ip, username=server.username, password=server.password)

    def run_cmd(cmd):
        stdin, stdout, stderr = ssh.exec_command(cmd)
        return stdout.read().decode().strip()

    return {
        "cpu_utilization": run_cmd("top -bn1 | grep 'Cpu(s)'"),
        "disk_space": run_cmd("df -h /"),
        "idle_time": run_cmd("w -s | head -1"),
        "last_write_time": run_cmd("ls -lt / | head -2 | tail -1 | awk '{print $6, $7, $8}'"),
        "last_write_path": run_cmd("ls -lt / | head -2 | tail -1 | awk '{print $9}'"),
        "last_logged_in_users": run_cmd("last -n 3"),
        "last_logged_in_time": run_cmd("last -n 1 | awk '{print $5, $6, $7}'"),
        "last_app_event_time": "N/A (not standard)"
    }

def fetch_windows_metrics(server):
    session = winrm.Session(f'http://{server.ip}:5985/wsman', auth=(server.username, server.password))

    def run_cmd(cmd):
        result = session.run_cmd(cmd)
        return result.std_out.decode().strip()

    return {
        "cpu_utilization": run_cmd("wmic cpu get loadpercentage"),
        "disk_space": run_cmd("wmic logicaldisk get size,freespace,caption"),
        "idle_time": "N/A",
        "last_write_time": run_cmd("powershell \"(Get-ChildItem C:\\ | Sort-Object LastWriteTime -Descending | Select -First 1).LastWriteTime\""),
        "last_write_path": run_cmd("powershell \"(Get-ChildItem C:\\ | Sort-Object LastWriteTime -Descending | Select -First 1).FullName\""),
        "last_logged_in_users": run_cmd("quser"),
        "last_logged_in_time": run_cmd("powershell \"(Get-EventLog -LogName Security -InstanceId 4624 | Select-Object -First 1).TimeGenerated\""),
        "last_app_event_time": run_cmd("powershell \"(Get-EventLog -LogName Application -Newest 1).TimeGenerated\"")
    }
