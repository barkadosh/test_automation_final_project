import subprocess


process = subprocess.Popen("C:\\Automation\\grafana-9.3.2.windows-amd64\\grafana-9.3.2\\bin\\grafana-server.exe "
                           "--homepath=C:\\Automation\\grafana-enterprise-9.3.2.windows-amd64\\grafana-9.3.2")

process.wait()