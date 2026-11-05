Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
 = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
 = New-Object System.Drawing.Bitmap .Width, .Height
 = [System.Drawing.Graphics]::FromImage()
.CopyFromScreen(.Location, [System.Drawing.Point]::Empty, .Size)
.Save('C:\Users\p-e-b\.gemini\antigravity-ide\brain\440a6412-d5d7-42a4-bf39-c16af339c78c\current_desktop_screen.png', [System.Drawing.Imaging.ImageFormat]::Png)
.Dispose()
.Dispose()
Write-Host 'Success'
