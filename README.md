# scrunch
Generate all possible password combinations from charset

It can be used for cracking WPA/WPA2 pre-shared keys with aircrack-ng or similar
to apply brute force.

## Getting Started
### WPA/WPA2 pre-shared keys

Catch WPA/WPA2 pre-shared keys.

Example:
```
airodump-ng -c CHANNEL --bssid AA:BB:CC:DD:EE:FF -w FILE-CAP MONITOR-INTERFACE-NAME
```

## How to run

Example 1:
Feed aircrack-ng with password generator output on charset "ABCDEFabcdef1234567890".
       5: Min password length: 5 symbols.
       8: Max password length: 8 symbols.
--no-rep: Each symbol can repeat only once.

```
python scrunch.pyc --no-rep 5 8 ABCDEFabcdef1234567890 | aircrack-ng -b AA:BB:CC:DD:EE:FF -w- *.cap
```

Example 2:
Generate wordlist.txt with all possible password combinations using all uppercase, all lowercase and all digits.

```
        5: Min password length: 5 symbols.
        5: Max password length: 5 symbols.
 --no-rep: Each symbol can repeat only once.
-ex ABCD: Exclude passwords that contain "ABCD" substring.
      -u: Include all uppercase letters
      -l: Include all lowercase letters
      -d: Include all decimal numbers
      -f: Write results to wordlist.txt
```

```
python scrunch.pyc --no-rep -u -l -d -ex ABCD -f wordlist.txt 5 5 DUMMY
```
For help use:

```
python scrunch.pyc -h
```

## Reference

Refer to the following tutorial for more details on how to get pre-shared keys.
https://www.aircrack-ng.org/doku.php?id=cracking_wpa

## Authors

* **Sergii Kriachko**


