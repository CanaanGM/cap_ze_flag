this repo is for challanges in https://play.picoctf.org/practice?originalEvent=70&page=1

the code can be sure be made 100x better buuuuuut it's gotta do one thing once so ¯\/(°_o)/¯ . . .

i've already done Includes ; once while the teacher was talking and the other watching him, so i'm not gonna include it.

#### challange basic_file_exploit : 
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

### Challange basic_mod1
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

### Challange basic_mod2
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

### Challange file types
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

