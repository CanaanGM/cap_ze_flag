this repo is for challanges in https://play.picoctf.org/practice?originalEvent=70&page=1

the code can be sure be made 100x better buuuuuut it's gotta do one thing once so ¯\/(°_o)/¯ . . .

i've already done Includes ; once while the teacher was talking and the other watching him, so i'm not gonna include it.

#### challange basic_file_exploit (2nd): 
<details>
<summary> /☠\ CODE /☠\ </summary>
    <div class="center"> 
        picoCTF{M4K3_5UR3_70_CH3CK_Y0UR_1NPU75_68466E2F}
    </div>
</details>

- steps:
    -  get their program and the source code
    - add an item / length
    - read the source code, realize what's at line 143
    - try to log it by giving it 0
    - ???
    - CODE !!

---

### Challange basic_mod1 (3rd)
<details>
<summary>/☠\ CODE /☠\ </summary>
    <div class="center"> 
    picoCTF{R0UND_N_R0UND_B6B25531}
    </div>
</details>

- steps:
    - read about cipher not cypher cause that will give u the 40k character (he's cool too) xD
        - https://sites.millersville.edu/bikenaga/number-theory/character-and-block-ciphers/character-and-block-ciphers.html
    - build a simple script "basic_mod_1.py", it's in the repo

---

### Challange basic_mod2 (4th)
<details>
<summary>/☠\ CODE /☠\ </summary>
    <div class="center"> 
        picoCTF{1NV3R53LY_H4RD_8A05D939}
    </div>
</details>

- steps:
    - /!\ there's a trick in the question so read carefully . . . 
    - read about the maths (⊙x⊙;)
    - adjust the basic_mod_1 script to solve this one
    - ???
    - profit !!!! 

--- 

### Challange file types (5th)
<details>
<summary>/☠\ CODE /☠\ </summary>
    <div class="center"> 
        picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_950c4fee}
    </div>
</details>

- steps:
    - /!\ this is tedious . . . 
    - open it with pestudio to see it's a shell file/script
    - extract it thru [unshar]
    - extract the result again thru [ar -x]
    - extract that into a Bzip archive thru [cpio -i]
    - extract it thru 7zip to get a Lzip
    - change the extension to lz and thru winrar
    - extract it to get an lz4 what the hell ?
    - extract it thru [lzip -d] dont overwrite!
    - u get something, extract it thru zip
    - mv the result so u can see it
    - yaaaay u got another archive !!
    - u'd get another lzip
    - open with winrar, ur prize is an xz
    - archive
    - u get a file with an ascii ??
    - decode it here https://www.dcode.fr/ascii-code
    - GG 
    - go take a walk or train i dunno ur mind needs it :X

---

### challange  CVE-XXXX-XXXX (6th)

<details>
<summary>/☠\ CODE /☠\ </summary>
    <div class="center"> 
        picoCTF{CVE-2021-34527}
    </div>
</details>

- steps
    - ask uncle google

--- 

### challange GDB Test Drive (7th)

<details>
<summary>/☠\ CODE /☠\ </summary>
    <div class="center"> 
        picoCTF{d3bugg3r_dr1v3_7776d758}
    </div>
</details>

- steps
    - follow instructions and debug the program

--- 

### challange buffer overflow (8th)

<details>
<summary>/☠\ CODE /☠\ </summary>
    <div class="center"> 
    picoCTF{ov3rfl0ws_ar3nt_that_bad_8ba275ff}
    </div>
</details>

- steps:
    - read the file, see the size limit
    - enter the biggest number u think of 


---

### challange credstuff (9th)

<details>
<summary>/☠\ CODE /☠\ </summary>
    <div class="center"> 
    picoCTF{C7r1F_54V35_71M3}
    </div>
</details>

- steps:
    - get the files 
    - load them into the script u've made
    - combine them
    - get the hashed code
    - google it to know the algo for hashing
    - decode it in python and print the result
    - ???
    - GG (script name is "leaking_passwords.py")

---

### challange enhance (10)

<details>
<summary>/☠\ CODE /☠\ </summary>
    <div class="center"> 
picoCTF{3nh4nc3d_d0a757bf}
    </div>
</details>

- steps:
    - get the image
    - open it in vscode
    - get the code at the bottom
    - copy it in python 
    - ` "c o d e ".replace(" ", "") `
    - copy it and paste it in the flag thingy


--- 


### challange file-run-1 (11)

<details>
    <summary>/☠\ CODE /☠\</summary>
    picoCTF{U51N6_Y0Ur_F1r57_F113_47cf2b7b}
</details>

- steps: 
    - get the code, move it into ur VM 
    - run it xD

--- 
### challange file-run-2 (12)

<details>
    <summary>/☠\ CODE /☠\</summary>
    picoCTF{F1r57_4rgum3n7_f65ed63e}
</details>

- steps: 
    - get the code, move it into ur VM 
    - run and greet it politly ヾ(•ω•`)o

--- 


### challange inspect HTML (13)

<details>
    <summary>/☠\ CODE /☠\</summary>
<tap>picoCTF{1n5p3t0r_0f_h7ml_fd5d57bd}</tap>
</details>

- steps:
    - inspect the HTML －O－

---

### challange local authority (14)

<details>
    <summary>/☠\ CODE /☠\</summary>
<tap>picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb} </tap>
</details>

- steps:
    - go to network tap 
    - log in
    - gg 
---

### challange lookey here (15)

<details>
    <summary>/☠\ CODE /☠\</summary>
<tap>picoCTF{gr3p_15_@w3s0m3_2116b979} </tap>
</details>

- steps:
    - get the file 
    - open it and ctr+f for pico
    - after reading the code yea i coulda used grep or findstr but i wanted to read the anthem anyways (￣o￣) . z Z . . .
---

### challange morse code (16)

<details>
    <summary>/☠\ CODE /☠\</summary>
<tap>picoCTF{wh47_h47h_90d_w20u9h7} </tap>
</details>

- steps:
    - get the file 
    - look for how to decode a morse code in python, find a module
    - create a script (morse_decoder.py) and volla ~!
---

### challange Sleuthkit intro (17)

<details>
    <summary>/☠\ CODE /☠\</summary>
<tap>picoCTF{mm15_f7w!} </tap>
</details>

- steps:
    - get the file -> unzip it 
    - mmls disk.img -> find length -> get code !
---

### challange Packets primer (18)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{p4ck37_5h4rk_01b0a0d6}
</details>

- steps:
    - get the file -> throw it in the VM -> wireshark 
    - get code -> decode Hex ? ASCII ? pokemon ?? anyways python replace space . . . CODE ?!!
        - https://www.dcode.fr/ascii-code
---

### challange Packets primer (19)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{C4n_Y0u_S33_m3_fully}
</details>

- steps:
    - get the file -> throw it in the VM -> Atril document viewer . . . GG

---

### challange rail-fence (20)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3}
</details>

- steps:
    - read about it 
    - look 4 a python example -> find [this implementaion ](https://www.geeksforgeeks.org/rail-fence-cipher-encryption-decryption/) 
    - get key

---

### challange patchme.py (21)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{p47ch1ng_l1f3_h4ck_21d62e33}
</details>

- steps:
    - get the py file
    - remove the checking and make it immediatly print the key xD 
    - profit

---

### challange Safe opener (22)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
</details>

- steps:
    - get the java source code
    - modify the code so it decodes and prints the decoded message 
    - ???  
    - profit

---

### challange substitution0 (22)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{5ub5717u710n_3v0lu710n_357bf9ff}
</details>

- steps:
    - visit uncle google, find [this](https://www.dcode.fr/monoalphabetic-substitution) 
    - python to lower the alpha 
    - got key!!

---


