Daily Auto Devops Bucket

# Prerequisite
- scoop [doc](https://github.com/ScoopInstaller/Install)
- rye [doc](https://rye-up.com/docs/getting-started/installation/)

# Install
```pwsh
scoop bucket add gauto "https://github.com/cel-ti/daily-auto"; Set-Location "$env:USERPROFILE\scoop\buckets\gauto"; python dauto/init.py
```
