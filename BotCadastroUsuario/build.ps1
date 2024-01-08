$exclude = @("venv", "BotCadastroUsuario.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BotCadastroUsuario.zip" -Force