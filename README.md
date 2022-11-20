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

### challange substitution0 (23)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{5ub5717u710n_3v0lu710n_357bf9ff}
</details>

- steps:
    - visit uncle google, find [this](https://www.dcode.fr/monoalphabetic-substitution) 
    - python to lower the alpha 
    - got key!!

---

### challange substitution1 (24)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoctf{fr3qu3ncy_4774ck5_4r3_c001_6e0659fb}
</details>

- steps:
    - stay at [this](https://www.dcode.fr/monoalphabetic-substitution), press auto decode
    - python to lower the alpha -> replace (j) -> (q) in the key 
    - got key!!

---

### challange substitution2 (25)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{n6r4m_4n41y515_15_73d10u5_42ea1770}
</details>

- steps:
    - use[this](https://planetcalc.com/8047/), calculate
    - gaze upon the mess !!  
    - getkeyfromthemessthatitgenerted!!

---

### challange transpositional-trial (26)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{7R4N5P051N6_15_3XP3N51V3_A9AFB178}
</details>

- steps:
    - did manually thru python cause i couldn't figure out why it ignores the braces in the string
    - get the code -> remove all spaces -> split at the count of 3 -> figure it out thru common sense . . . . 

---

### challange unpackme (27)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{175_chr157m45_85f5d0ac}
</details>

- steps:
    - make the program print 
    - ???
    - profit !

---

### challange vigenere (28)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_2951a89h}
</details>

- steps:
    - [dis](https://www.dcode.fr/vigenere-cipher) again 
    - ???
    - profit !

---

### challange bloat (29)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{d30bfu5c4710n_f7w_5e14b257}
</details>

- steps:
    - make the check return (True) instead of exiting hahaahahaha


---

### buffer overflow 1 (30)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{d30bfu5c4710n_f7w_5e14b257}
</details>

- steps:
    - get the vuln file 
    - `readelf -a vuln | grep win` (win is the function that gets called if u go to the correct address)
    - get the adress
    - apply [little endian](https://www.section.io/engineering-education/what-is-little-endian-and-big-endian/) cause i saw a 32 buffer
    - mess around in the terminal for 2 hrs
        - figure out that tacking the [little endian](https://www.section.io/engineering-education/what-is-little-endian-and-big-endian/) adress at the end will give u wierd symbols
        - find that there's a binary viewer in kali called `xxd`
        - pipe the result to it, yey adresss 
    - create a script to get u the key


---

### forbidden path (31)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{7h3_p47h_70_5ucc355_e5a6fcbc}
</details>

- steps:
    - `../` ur way to the flag


---

### freash java (32)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{700l1ng_r3qu1r3d_2bfe1a0d}
</details>

- steps:
    - use [JD-GUI](https://java-decompiler.github.io/)
    - open the class 
    - look for 10 mins cause `l` looked like a `1` (╯°□°）╯︵ ┻━┻
    - drink green tea
    - key


---

### power cookie (33)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{gr4d3_A_c00k13_0d351e23}
</details>

- steps:
    - crack the cokie for it is too old ! 


---

### RPS (34)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{50M3_3X7R3M3_1UCK_C85AF58A}
</details>

- steps:
    - get the source code
    - read source code 
    - 5 hrs later 
    - take each function and see what they do
    - strstr return a substring ; meaning it will look for the winner in the string u entered
    - play `rock\paper\scissors` 
    - break game
    - feel good -> key ~! 


---

### SQLLite (35)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{L00k5_l1k3_y0u_solv3d_it_ec8a64c7}
</details>

- steps:
    - basic Sql syntax 
    - `' OR 1=1;` in the pass field which tells lite that the first half can be right 
    - inspect hidden `<p>` 
    - get code ~ !


---

### Sleuthkit Apprentice (36)

<details>
    <summary>/☠\ CODE /☠\</summary>
picoCTF{by73_5urf3r_2f22df38}
</details>

- steps:
    - get the file , unzip it  
    - try to mount it like a normal image and dig thru the files, didn't work
    - followed [this](https://dev.iachieved.it/iachievedit/exploring-img-files-on-linux/) to no avail
    - google what the hell is a sleuthkit ?!
    - start autopsy in kali
    - load the image, create a new investigation . . . 
    - select the biggest image cause that's the file system, `1` is boot `2` is swap
    - Analyze -> keyword search for `picoCTF` . . . nothing, try `flag.txt`, found it but it's useless QAQ
    - spend sometime looking
    - try to file name search for `flag.txt` in `file analysis` tab . . . got a location!!
    - export it . . . nothing o(≧口≦)o but we got a location which is `/3/root/my_folder`
    - go there, export both flag files -> open in VScode -> Celebrate!!


---




