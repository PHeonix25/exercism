param(
    # Choose which language you want to process
    [Parameter(Mandatory)]
    [string]$Language,
    
    # Override the path to Exercism projects
    [Parameter()]
    [string]$ExercismPath
)

# Validate that Excism exists... and if it does, pull out the base directory
if ([string]::IsNullOrEmpty($ExercismPath)) {
    $ExercismPath = ((exercism configure | Select-String -Pattern "--dir=") -replace "--dir=","").Trim()
    $LanguagePath = Join-Path -Path $ExercismPath $Language;
    Write-Host -ForegroundColor Green "Exercism path located at '$ExercismPath'";
}

# Check that the language that the user wants to use is "valid"...
$LanguageInvalid = (exercism status $Language 2>&1) | Out-String | Select-String -Pattern "There is no track with ID" -Quiet
if ($LanguageInvalid) {
    Write-Host "";
    Write-Host -ForegroundColor Red " '$Language' is not a valid ""language track"" ID.";
    Write-Host -ForegroundColor Red " Please provide a valid language track ID.";
    Write-Host -ForegroundColor Red " You can find a list of ""language track ID's"" by running ``exercism track``";
    Write-Host "";
    return;
} elseif (!(Test-Path -Path $LanguagePath)) { # ...and that they have started on the challenge
    Write-Host "";
    Write-Host -ForegroundColor Red " '$LanguagePath' is not a valid path.";
    Write-Host -ForegroundColor Red " Please pull down the first '$Language' challenge before running this script.";
    Write-Host "";
    return;
}

# Change into the Language directory, everything else is based off this.
Push-Location $LanguagePath
Write-Verbose "Changing to 'LanguagePath' directory: $LanguagePath"

# Create the solution file (if necessary)
$SolutionFile = "$Language.sln"
$SolutionFilePath = Join-Path $LanguagePath $SolutionFile
$SolutionFileExists = Test-Path -Path $SolutionFilePath -PathType Leaf 
if ($SolutionFileExists) {
    Write-Host -ForegroundColor Green "Existing solution file located at $SolutionFilePath"
} else {
    Write-Host -ForegroundColor Yellow "Existing solution file not located. New '$Language' solution file required." 
    Write-Host -ForegroundColor Yellow "Creating solution file at '$SolutionFilePath'";
    & dotnet new sln;
    if (Test-Path -Path $SolutionFilePath -PathType Leaf) {
        Write-Host -ForegroundColor Green "Solution file created successfully at '$SolutionFilePath'";
    } else {
        Write-Host "";
        Write-Host -ForegroundColor Red "Something went wrong while creating the solution file.";
        Write-Host -ForegroundColor Red "Please check the errors listed above and try again."
        Pop-Location; return;
    }
}

# Unfortunately, we need some f*ckery to create a new class lib project in either F# or C# at the moment
# For more details, please see here: https://github.com/dotnet/netcorecli-fsc/issues/103 
# Hopefully this requirement will go away when this issue is closed: https://github.com/exercism/xfsharp/issues/308
$dotnetNewCommand = "dotnet new classlib -all"
if ($Language -match "fsharp") { 
    $dotnetNewCommand += " --language F#" # Thankfully F# defaults to `netstandard1.6`
} else {
    $dotnetNewCommand += " --framework netstandard1.6"
}

# Loop through each challenge that's currently there and make a project out of it...
$ChallengeDirectories = Get-ChildItem $LanguagePath | Where-Object {$_.PSISContainer}
foreach ($dir in $ChallengeDirectories) {
    Write-Verbose "Changing into challenge directory '$dir'."
    Push-Location $dir;
    Write-Verbose "Creating new Class Library with command '$dotnetNewCommand'";
    Invoke-Expression $dotnetNewCommand;
    $projectPath = (Resolve-Path *proj).Path
    if (Test-Path -Path $projectPath -PathType Leaf) {
        Write-Host -ForegroundColor Green "Class Library Project created successfully at '$projectPath'";
    } else {
        Write-Host "";
        Write-Host -ForegroundColor Red "Something went wrong while creating the project file.";
        Write-Host -ForegroundColor Red "Please check the errors listed above and try again."
        Pop-Location; return;
    }
    Pop-Location;
    
    Write-Verbose "Adding project '$projectPath' to '$SolutionFile'."
    & dotnet sln $SolutionFile add $projectPath;
    Write-Host -ForegroundColor Green "Reference to project has been added to parent solution."
    
    Push-Location $dir;
    Write-Verbose "Adding commonly required dependencies to the project"
    & dotnet add package NUnit -s https://api.nuget.org/v3/index.json
    & dotnet add package NUnit.ConsoleRunner -s https://api.nuget.org/v3/index.json
    & dotnet add package NUnit3TestAdapter -s https://api.nuget.org/v3/index.json
    & dotnet add package Microsoft.TestPlatform.TestHost -s https://api.nuget.org/v3/index.json
    Write-Host -ForegroundColor Green "Required common packages added successfully."
    Pop-Location;
    
    Push-Location $dir;
    Write-Verbose "Restoring the packages, and trying to run the challenge"
    & dotnet restore --verbosity=quiet -s https://api.nuget.org/v3/index.json
    Write-Host -ForegroundColor Green "Restoration of packages completed successfully."
    & dotnet build --verbosity=quiet
    Write-Host -ForegroundColor Green "Build of your solution was fine. Go Ace!"
    & dotnet test $projectPath
    Write-Host -ForegroundColor Green "Guess the tests passed too... Nice work!"
    Pop-Location;
}

Write-Host "Thanks for using the tool, lets put you back in the right folder, and launch the complete solution :)"
Start-Process *.sln;
Pop-Location;