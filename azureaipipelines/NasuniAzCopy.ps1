<#
.SYNOPSIS
Copy data between an NEA mounted fileshare to Azure Container as part of an AI Pipeline

.DESCRIPTION 
This is an example powershell script to easily copy data from a Nasuni Edge Appliance mounted on the local windows machine and copy it to a storage container as part of an AI pipeline. As described: https://github.com/nasuni-labs/nasuni-ai/blob/main/azureaipipelines/Nasuni-%20AzCopy%20technical%20white%20paper%20.pdf

.PARAMETER DirPath
Use Dirpath to specify the path to NEA that you want to start the copy of data.

.PARAMETER ContainerName
Use ContainerName to specify the name of the cotainer you are copying the the data into as part of your AI Pipeline.

.PARAMETER StorageAcctName
Use StorageAcctName to specify the name of the Storage Account you will be using for the above container.

.PARAMETER SASToken
Use SASToken to specify the SAS Token for authentication to the above Storage Account/Container

.PARAMETER Recusive 
Use Recusrive to specify if you want a recusive copy of data starting at DirPath

.PARAMETER WildcardFileName
Use WildcardFileName if you want to specify only specific file names/types to be copied

.EXAMPLE
.\NasuniAzCopy.ps1 -Dirpath "N:\Nasuni Flies\Home Directories\jliddle\demo data" -ContainerName "yourcontainer" -StorageAcctName "yourstorageaccount" -SASToken "?xxxx" -WildcardFileName "*.pdf" -Recusrive $true
#>


param (
    [Parameter(Mandatory=$true)]
    [string]$DirPath,
    [Parameter(Mandatory=$true)]
    [string]$ContainerName,
    [Parameter(Mandatory=$true)]
    [string]$StorageAcctName,
    [Parameter(Mandatory=$true)]
    [string]$SASToken,
    [switch]$Recursive,
    [string]$WildcardFileName = "*"
)


#Change your path here to the location of your azcopy.exe install
$AzCopyPath = "C:\Program Files\Microsoft\AzCopy\azcopy.exe"

$Command = "$AzCopyPath copy `"$DirPath\$WildcardFileName`" `"https://$StorageAcctName.blob.core.windows.net/$ContainerName`$SASToken`" --recursive=$Recursive --log-level=INFO"

Write-Host "Running command: $Command"
Invoke-Expression $Command
