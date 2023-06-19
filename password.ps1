$length = Read-Host "Enter the desired password length"
$includeUppercase = Read-Host "Include uppeercase letters? (Y/N)"
$includeLowercase = Read-Host "Include lowercase letters? (Y/N)"
$includeDigits = Read-Host "Include digits? (Y/N)"
$includeSpecialChars = Read-Host "Include special characters? (Y/N)"
$numberOfPasswords = Read-Host "Enter the number of passwords to generate"

# Defining user inputs, defining the characters sets that will be used to generate the passwords

$uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
$lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
$digits = "0123456789"
$specialchars = "!@#$%^&*()-=_+?/"

# writing a loop to generate the desired number of passwords. 
# within loop, randomly selecting characters 
# concatenate them to form a password of the desired length

for ($i = 1; $i -le $numberOfPasswords) {  
    $password = ""
    for ($j = 1; $j -le $length; $j++) { # nested loop that will run for specified length 
    # starts $j variable to 1 and continues looping as long as $j is less than or equal to specified length

        if ($includeUppercase -eq "Y") {  # checks if user specified to include uppercase letters   
	        $password += $uppercaseLetters[(Get-Random - Minimum 0 -Maximum $uppercaseLetters.Length)]

        # generates random numbers bw 0 and length of the $uppercaseLetters string
        # then uses that number as an index to select a random uppercase letter from the string
        }
        if ($includeLowercase -eq "Y") {  # checks if user specified to include lowercase letters
            $password += $lowercaseLetters[(Get-Random - Minimum 0 -Maximum $lowercaseLetters.Length)] 
              
        # generates random numbers between 0 and length of the $lowercaseLetters string
        # then uses that number as an index to select a random lowercase letter from the string
        }
        if ($includeDigits -eq "Y") {
            $password += $digits[(Get-Random -Minimum 0 -Maximum $digits.Length)]
        }
        if ($includespecialchars -eq "Y") {
            $password += $specialchars[(Get-Random -Minimum 0 -Maximum $specialchars.Length)]
        }
    }
    Write-Host "Generated Password: $password"
}

# Display/Export Passwords
# Should display generated password to the console 

Write-Host "Password generation completed."

# Export password to a file 
$passwords | Out-File -FilePath "C:\shihe\to\password.txt"
Write-Host "Passwords exported to passwords.txt"
