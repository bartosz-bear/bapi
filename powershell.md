# Powershell

<https://www.guru99.com/powershell-tutorial.html>

## Basics

- PowerShell allows access to all the types in the .NET framework
- PowerShell allows scripts and cmdlets to be invoked on a remote machine
- scripts and pipelines can be invoked asynchronously
- PowerShell supports a specialized type of Network File Transfer using Background Intelligent Transfer Service (BITS)

## How do you check PowerShell version?

```ps
$PSVersionTable

Name                           Value
----                           -----
PSVersion                      5.1.19041.2364
PSEdition                      Desktop
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}
BuildVersion                   10.0.19041.2364
CLRVersion                     4.0.30319.42000
WSManStackVersion              3.0
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1
```

## How do you run a PowerShell script from current directory?

```ps
.\my_script.ps1
```

## How do you run a PowerShell script from `cmd.exe`?

```ps
powershell -noexit "& ""C:\my_script.ps1"""
```

## How do you clear the command prompt?

```ps
clear
```

## How do you print a message?

```ps
Write-Host "Hello, world!"
```

## cmdlet - command lets

`cmdlet` is a lightweight command used in the Windows based PowerShell environment

- most of the PowerShell functionality comes from cmdlet is always in verb-noun format, separated by a hyphen and not plural (eg. `Get-Help`, Get-verb, Help-noun)
- cmdlets are .NET framework class objects
- cmdlets return objects not text
- cmdlet is a series of commands, which is more tahn one line, stored in a text file with a `.ps1` extension

## Important commands

- `Get` - to get something
- `Start` - to run something
- `Out` - to output something
- `Stop` - to stop something that is running
- `Set` - to define something
- `New` - to create something

### `Get-Help`

Displays help information about commands and topics

```ps
Get-Help Format-Table
```

### `Get-Command`

Get information about all functions and cmdlets which can be invoked on the machine

```ps
Get-Command
```

### How do you create a new folder?

```ps
New-Item -Path 'C:\Users\User\Desktop\TestFolder' -ItemType Directory
```

### Special variables

- `$Error`- an array of the most recent error objects
- `$Host` - name of the current hosting application
- `$Profile` - path of the user profile
- `$PID` - process identifier
- `$Null` - contains a NULL value
- `$False` - contains FALSE value
- `$True` - contains TRUE value