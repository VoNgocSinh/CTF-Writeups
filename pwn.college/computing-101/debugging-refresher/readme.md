# Pwn.college - writeups CTF

- **Challenge:** Debugging Refresher Level 1 -> 8
- **Category:** Programming languages
- **Difficulty:** Easy
- **Source**: [pwn.college](https://pwn.college/computing-101/debugging-refresher/)

**📝Note:** Xhi chào các bạn! Trong ```writeup``` này mình sẽ chia sẻ lại hành trình học và làm các thử thách về Debugging từ level 1 đến 30. Mình chọn pwn.college
 làm nơi bắt đầu vì đây là một khóa học rất trực quan, dễ tiếp cận cho người mới. Hy vọng writeup này sẽ giúp các bạn mới bắt đầu có thêm tài liệu tham khảo và cảm thấy Debugging bớt “khó nhằn” hơn. 

---
 
### Level 1 - Debugging Programs

This level gets you re-familiarized with gdb.
To get started with this level, and all the other levels of this module, run `/challenge/embryogdb_levelXYZ`, where XYZ is the level number.
That program will launch `gdb`.
Run the actual level logic with `r`, and follow the prompts to get that flag!

---
**RELEVANT DOCUMENTATION:**
- gdb's [run](https://sourceware.org/gdb/current/onlinedocs/gdb#Starting) command
- gdb's [continue](https://sourceware.org/gdb/current/onlinedocs/gdb#Continuing-and-Stepping) command

---

#### Solution

Bài này mình sẽ thực thi file `/challenge/embryogdb_level1`. Khi file được thực thi thì thấy đã tích hợp sẵn trình debug khi khởi chạy. Sau đó mình sẽ thử sử dụng `run` (để run file trong gdb) và `continue` (để tiếp tục chạy tiếp file cho tới mục tiêu tiếp theo).

    hacker@debugging-refresher~debugging-programs:/challenge$ ls
    DESCRIPTION.md  embryogdb_level1
    hacker@debugging-refresher~debugging-programs:/challenge$ ./embryogdb_level1 
    .
    .
    .
    (gdb) run
    Starting program: /challenge/embryogdb_level1 
    ###
    ### Welcome to /challenge/embryogdb_level1!
    ###
    .
    .
    .
    (gdb) continue
    Continuing.
    You win! Here is your flag:
    pwn.college{EVh3iF3LlHqXajzGrMM_Lk8Hslo.dRDNywCMxADNwEzW}


    [Inferior 1 (process 277) exited normally]
    (gdb) 

---

#### Flag
    pwn.college{EVh3iF3LlHqXajzGrMM_Lk8Hslo.dRDNywCMxADNwEzW}

---

### Level 2 - Inspecting Registers

Next, we'll learn about how to print out the values of registers.

You can see the values for all your registers with `info registers`. Alternatively, you can also just print a particular
register's value with the `print` command, or `p` for short. For example, `p $rdi` will print the value of $rdi in
decimal. You can also print its value in hex with `p/x $rdi`.

In order to solve this level, you must figure out the current random value of register r12 in hex.

As before, start the challenge, invoke the `run` gdb command, then follow the instructions.
When you've printed out what you need, remember to `continue` to move on to the next step of the challenge!

----
**RELEVANT DOCUMENTATION:**
- gdb's [run](https://sourceware.org/gdb/current/onlinedocs/gdb#Starting) command
- gdb's [continue](https://sourceware.org/gdb/current/onlinedocs/gdb#Continuing-and-Stepping) command
- gdb's [info](https://sourceware.org/gdb/current/onlinedocs/gdb#Registers) command
- gdb's [print](https://sourceware.org/gdb/current/onlinedocs/gdb#Data) command

---

#### Solution

Cấp độ này yêu cầu mình đoán 1 giá trị random nào đó để get được flag. 

    (gdb) run
    Starting program: /challenge/embryogdb_level2 
    ###
    ### Welcome to /challenge/embryogdb_level2!
    ###

    .
    .
    .

    The random value has been set!


    Program received signal SIGTRAP, Trace/breakpoint trap.
    0x000058f66dd87bfd in main ()
    (gdb) c
    Continuing.
    Random value: 123456
    You input: 123456
    The correct answer is: 8fd3c227350dad85
    [Inferior 1 (process 170) exited with code 01]
    (gdb) 

Như yêu cầu của level sẽ có hướng dẫn về xem thông tin của các thanh ghi (`info registers`). Vì vậy theo mình nghĩ giá trị random đó sẽ được save ở trong thanh ghi nào đó cho nên trước khi `continue` mình sẽ in ra info của các thanh ghi và đối chiếu với giá trị random được cho ở cuối chương trình để xem nó nằm ở thanh ghi nào.

    (gdb) info register
    rax            0x20                32
    rbx            0x5b7fc382dcb0      100604299107504
    rcx            0x7bf141ae3297      136276119270039
    rdx            0x0                 0
    rsi            0x7bf141bc2723      136276120184611
    rdi            0x7bf141bc37e0      136276120188896
    rbp            0x7ffd8f4eab70      0x7ffd8f4eab70
    rsp            0x7ffd8f4eab30      0x7ffd8f4eab30
    r8             0x20                32
    r9             0x2c                44
    r10            0x0                 0
    r11            0x246               582
    r12            0x9474d5e7058516a0  -7749333870591011168
    r13            0x7ffd8f4eac60      140727007751264
    r14            0x0                 0
    r15            0x0                 0
    rip            0x5b7fc382dbfd      0x5b7fc382dbfd <main+343>
    eflags         0x246               [ PF ZF IF ]
    cs             0x33                51
    ss             0x2b                43
    ds             0x0                 0
    es             0x0                 0
    fs             0x0                 0
    gs             0x0                 0
    (gdb) continue
    Continuing.
    Random value: 123456
    You input: 123456
    The correct answer is: 9474d5e7058516a0
    [Inferior 1 (process 202) exited with code 01]
    (gdb) 

Như ta có thể thấy rõ ở trên, giá trị random được save tại thanh ghi `r12`. Vì thế trước khi `continue` mình sẽ in ra giá trị của thanh ghi `r12` rồi nhập vào input để get được flag.

    (gdb) p/x $r12
    $2 = 0xfc74831d567fa671
    (gdb) c
    Continuing.
    Random value: 0xfc74831d567fa671
    You input: fc74831d567fa671
    The correct answer is: fc74831d567fa671
    You win! Here is your flag:
    pwn.college{gIsXg_Ogn5SMspTBRZ8tmMD71pw.dVDNywCMxADNwEzW}


    [Inferior 1 (process 207) exited normally]
    (gdb) 

---

#### Flag
    pwn.college{gIsXg_Ogn5SMspTBRZ8tmMD71pw.dVDNywCMxADNwEzW}

---

### Level 3 - Examining Memory

Next, we'll learn to use gdb to peek into process memory!

You can e**x**amine the contents of memory using the `x/<n><u><f> <address>` parameterized command. In this format `<u>` is
the unit size to display, `<f>` is the format to display it in, and `<n>` is the number of elements to display. Valid
unit sizes are `b` (1 byte), `h` (2 bytes), `w` (4 bytes), and `g` (8 bytes). Valid formats are `d` (decimal), `x`
(hexadecimal), `s` (string) and `i` (instruction). The address can be specified using a register name, symbol name, or
absolute address. Additionally, you can supply mathematical expressions when specifying the address.

For example, `x/8i $rip` will print the next 8 instructions from the current instruction pointer. `x/16i main` will
print the first 16 instructions of main. You can also use `disassemble main`, or `disas main` for short, to print all of
the instructions of main. Alternatively, `x/16gx $rsp` will print the first 16 values on the stack. `x/gx $rbp-0x32`
will print the local variable stored there on the stack.

You will probably want to view your instructions using the CORRECT assembly syntax. You can do that with the command
`set disassembly-flavor intel`.

In order to solve this level, you must figure out the random value on the stack (the value read in from `/dev/urandom`).
Think about what the arguments to the read system call are.

----
**RELEVANT DOCUMENTATION:**
- gdb's [run](https://sourceware.org/gdb/current/onlinedocs/gdb#Starting) command
- gdb's [continue](https://sourceware.org/gdb/current/onlinedocs/gdb#Continuing-and-Stepping) command
- gdb's [info](https://sourceware.org/gdb/current/onlinedocs/gdb#Registers) command
- gdb's [print](https://sourceware.org/gdb/current/onlinedocs/gdb#Data) command
- gdb's [examine](https://sourceware.org/gdb/current/onlinedocs/gdb#Memory) command

---

#### Solution

Tương tự như level trước, bài này yêu cầu mình đoán 1 giá trị random nào đó để get được flag. Tuy nhiên giá trị đó sẽ không được lưu ở trên thanh ghi nào đó mà nó được lưu ở trên stack. Để cụ thể hơn mình sẽ sử dụng `disas main` xem các lệnh ở trong chương trình để biết nó được lưu ở đâu trên stack.

    ...
    0x00006510ecbc0cb4 <+526>:   mov    $0x0,%eax
    0x00006510ecbc0cb9 <+531>:   callq  0x6510ecbc01d0 <printf@plt>
    0x00006510ecbc0cbe <+536>:   mov    -0x10(%rbp),%rdx
    0x00006510ecbc0cc2 <+540>:   mov    -0x18(%rbp),%rax
    0x00006510ecbc0cc6 <+544>:   cmp    %rax,%rdx
    0x00006510ecbc0cc9 <+547>:   je     0x6510ecbc0cd5 <main+559>
    0x00006510ecbc0ccb <+549>:   mov    $0x1,%edi
    0x00006510ecbc0cd0 <+554>:   callq  0x6510ecbc0280 <exit@plt>
    0x00006510ecbc0cd5 <+559>:   addl   $0x1,-0x1c(%rbp)
    0x00006510ecbc0cd9 <+563>:   cmpl   $0x0,-0x1c(%rbp)
    0x00006510ecbc0cdd <+567>:   jle    0x6510ecbc0c2c <main+390>
    0x00006510ecbc0ce3 <+573>:   mov    $0x0,%eax
    0x00006510ecbc0ce8 <+578>:   callq  0x6510ecbc097d <win>
    ...

Như có thể thấy ở trên, lệnh `cmp` so sánh 2 thanh ghi `rax` và `rdx`. Mà 2 thanh ghi đó lấy giá trị từ stack với địa chỉ lần lượt là `-0x10(%rbp)` và `-0x18(%rbp)`. Nếu đọc các lệnh phía trên sâu hơn nữa thì có thể quan sát thấy giá trị mình nhập vào sẽ được lưu ở `-0x10(%rbp)` còn giá trị target sẽ được lưu ở `-0x18(%rbp)`. Vì vậy mình sẽ in ra giá trị của địa chỉ `-0x18(%rbp)` để biết giá trị target sau đó nhập vào input.

    (gdb) c
    Continuing.
    The random value has been set!


    Program received signal SIGTRAP, Trace/breakpoint trap.
    0x000062f9d7090c64 in main ()
    (gdb) x/gx $rbp-0x18
    0x7ffcd08c7748: 0x3906158cdb400d19
    (gdb) c
    Continuing.
    Random value: 0x3906158cdb400d19
    You input: 3906158cdb400d19
    The correct answer is: 3906158cdb400d19
    You win! Here is your flag:
    pwn.college{k4iAx4dx9jv0tiDW1dBhx_bpBK8.dZDNywCMxADNwEzW}


    [Inferior 1 (process 203) exited normally]
    (gdb) 

---

#### Flag
    pwn.college{k4iAx4dx9jv0tiDW1dBhx_bpBK8.dZDNywCMxADNwEzW}

---

### Level 4 - Settings Breakpoints

A critical part of dynamic analysis is getting your program to the state you are interested in analyzing.
So far, these challenges have automatically set breakpoints for you to pause execution at states you may be interested in analyzing.
It is important to be able to do this yourself.

There are a number of ways to move forward in the program's execution.
You can use the `stepi <n>` command, or `si <n>` for short, in order to step forward one instruction.
You can use the `nexti <n>` command, or `ni <n>` for short, in order to step forward one instruction, while stepping over any function calls.
The `<n>` parameter is optional, but allows you to perform multiple steps at once.
You can use the `finish` command in order to finish the currently executing function.
You can use the `break *<address>` parameterized command in order to set a breakpoint at the specified-address.
You have already used the `continue` command, which will continue execution until the program hits a breakpoint.

While stepping through a program, you may find it useful to have some values displayed to you at all times.
There are multiple ways to do this.
The simplest way is to use the `display/<n><u><f>` parameterized command, which follows exactly the same format as the `x/<n><u><f>` parameterized command.
For example, `display/8i $rip` will always show you the next 8 instructions.
On the other hand, `display/4gx $rsp` will always show you the first 4 values on the stack.
Another option is to use the `layout regs` command.
This will put gdb into its TUI mode and show you the contents of all of the registers, as well as nearby instructions.

In order to solve this level, you must figure out a series of random values which will be placed on the stack.
As before, `run` will start you out, but it will interrupt the program and you must, carefully, continue its execution.

You are highly encouraged to try using combinations of `stepi`, `nexti`, `break`, `continue`, and `finish` to make sure you have a good internal understanding of these commands.
The commands are all absolutely critical to navigating a program's execution.

----
**RELEVANT DOCUMENTATION:**
- gdb's [run](https://sourceware.org/gdb/current/onlinedocs/gdb#Starting) command
- gdb's [continue](https://sourceware.org/gdb/current/onlinedocs/gdb#Continuing-and-Stepping) command
- gdb's [info](https://sourceware.org/gdb/current/onlinedocs/gdb#Registers) command
- gdb's [print](https://sourceware.org/gdb/current/onlinedocs/gdb#Data) command
- gdb's [examine](https://sourceware.org/gdb/current/onlinedocs/gdb#Memory) command
- gdb's [break](https://sourceware.org/gdb/current/onlinedocs/gdb#Set-Breaks) command
- gdb's [display](https://sourceware.org/gdb/current/onlinedocs/gdb#Auto-Display) command
- gdb's [various stepping commands](https://sourceware.org/gdb/current/onlinedocs/gdb#Continuing-and-Stepping) command (that whole section)

**NOTE:**
This challenge will require you to _read_ and _understand_ assembly!
Don't worry, this skill will come in quite handy later in pwn.college.

---

#### Solution

Cấp độ này mình sẽ sử dụng breakpoint. Vì giá trị random được set trước khi yêu cầu nhập input vì thế nên mình sẽ đặt breakpoint ngay sau khi giá trị random được set, sau đó mình sẽ leak giá trị đó và nhập vào input.

    (gdb) b*0x000062d4a2fd6ccf
    Breakpoint 1 at 0x62d4a2fd6ccf
    (gdb) c
    Continuing.
    The random value has been set!

    Random value: 
    Breakpoint 1, 0x000062d4a2fd6ccf in main ()
    (gdb) x/gx $rbp-0x18
    0x7ffeb813adf8: 0xc1ba140da60f9380

    (gdb) ni
    0x000062d4a2fd6cd6 in main ()
    (gdb) c
    Continuing.
    0xc1ba140da60f9380
    You input: c1ba140da60f9380
    The correct answer is: c1ba140da60f9380
    The random value has been set!

    Random value: 
    Breakpoint 1, 0x000062d4a2fd6ccf in main ()

    (gdb) x/gx $rbp-0x18
    0x7ffeb813adf8: 0xa89c8937186272b3

    (gdb) c
    Continuing.
    0xa89c8937186272b3
    You input: a89c8937186272b3
    The correct answer is: a89c8937186272b3
    The random value has been set!

    Random value: 
    Breakpoint 1, 0x000062d4a2fd6ccf in main ()
    (gdb) x/gx $rbp-0x18
    0x7ffeb813adf8: 0x72f6c5d876eeb172

    (gdb) c
    Continuing.
    0x72f6c5d876eeb172
    You input: 72f6c5d876eeb172
    The correct answer is: 72f6c5d876eeb172
    The random value has been set!

    Random value: 
    Breakpoint 1, 0x000062d4a2fd6ccf in main ()
    (gdb) x/gx $rbp-0x18
    0x7ffeb813adf8: 0x8c279d62bde2d342

    (gdb) c
    Continuing.
    0x8c279d62bde2d342
    You input: 8c279d62bde2d342
    The correct answer is: 8c279d62bde2d342
    You win! Here is your flag:
    pwn.college{gD1dndoU1QfPadn4WdVZ05nFGRe.ddDNywCMxADNwEzW}

    (gdb) 

---

#### Flag
    pwn.college{gD1dndoU1QfPadn4WdVZ05nFGRe.ddDNywCMxADNwEzW}

---

### Level 5 - GDB Scripting

---

We write code in order to express an idea which can be reproduced and refined.
We can think of our analysis as a program which injests the target to be analyzed as data.
As the saying goes, code is data and data is code.

While using gdb interactively as we've done with the past levels is incredibly powerful, another powerful tool is gdb scripting.
By scripting gdb, you can very quickly create a custom-tailored program analysis tool.
If you know how to interact with gdb, you already know how to write a gdb script--the syntax is exactly the same.
You can write your commands to some file, for example `x.gdb`, and then launch gdb using the flag `-x <PATH_TO_SCRIPT>`.
This file will execute all of the gdb commands after gdb launches.
Alternatively, you can execute individual commands with `-ex '<COMMAND>'`.
You can pass multiple commands with multiple `-ex` arguments.
Finally, you can have some commands be always executed for any gdb session by putting them in `~/.gdbinit`.
You probably want to put `set disassembly-flavor intel` in there.

Within gdb scripting, a very powerful construct is breakpoint commands. Consider the following gdb script:

```gdb
start
break *main+42
commands
  x/gx $rbp-0x32
  continue
end
continue
```

In this case, whenever we hit the instruction at `main+42`, we will output a particular local variable and then continue execution.

Now consider a similar, but slightly more advanced script using some commands you haven't yet seen:

```gdb
start
break *main+42
commands
  silent
  set $local_variable = *(unsigned long long*)($rbp-0x32)
  printf "Current value: %llx\n", $local_variable
  continue
end
continue
```

In this case, the `silent` indicates that we want gdb to not report that we have hit a breakpoint, to make the output a bit cleaner.
Then we use the `set` command to define a variable within our gdb session, whose value is our local variable.
Finally, we output the current value using a formatted string.

Use gdb scripting to help you collect the random values in this level.
This may feel difficult, but will serve you well in your journey ahead.

----
**RELEVANT DOCUMENTATION:**
- gdb's [run](https://sourceware.org/gdb/current/onlinedocs/gdb#Starting) command
- gdb's [continue](https://sourceware.org/gdb/current/onlinedocs/gdb#Continuing-and-Stepping) command
- gdb's [info](https://sourceware.org/gdb/current/onlinedocs/gdb#Registers) command
- gdb's [print](https://sourceware.org/gdb/current/onlinedocs/gdb#Data) command
- gdb's [examine](https://sourceware.org/gdb/current/onlinedocs/gdb#Memory) command
- gdb's [break](https://sourceware.org/gdb/current/onlinedocs/gdb#Set-Breaks) command
- gdb's [display](https://sourceware.org/gdb/current/onlinedocs/gdb#Auto-Display) command
- gdb's [various stepping commands](https://sourceware.org/gdb/current/onlinedocs/gdb#Continuing-and-Stepping) command (that whole section)
- gdb's [breakpoint scripting](https://sourceware.org/gdb/current/onlinedocs/gdb#Break-Commands)


---

#### Solution
Cấp độ này yêu cầu mình viết script để xử lí các công việc lặp đi lặp lại trong khi debug hoặc có thể giúp mình nhanh hơn trong khi debug. Ví thế mình sẽ viết 1 shellscript gdb như bên dưới để giúp mình đặt breakpoint sau đó in ra thông tin của giá trị random đó và mình chỉ cần copy và parse vào input là xong.

```shell
start
break *main+752
continue
commands
  x/gx $rbp-0x18
  continue
end
continue
```


    ...
    Program received signal SIGTRAP, Trace/breakpoint trap.
    0x00005c5e043e3d33 in main ()
    The random value has been set!

    Random value: 
    Breakpoint 2, 0x00005c5e043e3d96 in main ()
    0x7fff44f14878: 0xa064fedebc62d676
    0xa064fedebc62d676
    You input: a064fedebc62d676
    The correct answer is: a064fedebc62d676
    The random value has been set!

    ...

    Random value: 
    Breakpoint 2, 0x00005c5e043e3d96 in main ()
    0x7fff44f14878: 0xa40380b74c94ac6b
    0xa40380b74c94ac6b
    You input: a40380b74c94ac6b
    The correct answer is: a40380b74c94ac6b
    The random value has been set!

    Random value: 
    Breakpoint 2, 0x00005c5e043e3d96 in main ()
    --Type <RET> for more, q to quit, c to continue without paging--
    0x7fff44f14878: 0x4388304ed9788f9e
    0x4388304ed9788f9e
    You input: 4388304ed9788f9e
    The correct answer is: 4388304ed9788f9e
    You win! Here is your flag:
    pwn.college{0Fz9f9oScnJv4t4olpXmaztPTAN.dhDNywCMxADNwEzW}


    [Inferior 1 (process 266) exited normally]
    (gdb) Quit
    (gdb) Quit
    (gdb) 

---

#### Flag
    pwn.college{0Fz9f9oScnJv4t4olpXmaztPTAN.dhDNywCMxADNwEzW}

---

### Level 6 - Modifying Data

---

As it turns out, gdb has FULL control over the target process.
Not only can you analyze the program's state, but you can also modify it.
While gdb probably isn't the best tool for doing long term maintenance on a program, sometimes it can be useful to quickly modify the behavior of your target process in order to more easily analyze it.

You can modify the state of your target program with the `set` command.
For example, you can use `set $rdi = 0` to zero out $rdi.
You can use `set *((uint64_t *) $rsp) = 0x1234` to set the first value on the stack to 0x1234.
You can use `set *((uint16_t *) 0x31337000) = 0x1337` to set 2 bytes at 0x31337000 to 0x1337.

Suppose your target is some networked application which reads from some socket on fd 42.
Maybe it would be easier for the purposes of your analysis if the target instead read from stdin.
You could achieve something like that with the following gdb script:

```gdb
start
catch syscall read
commands
  silent
  if ($rdi == 42)
    set $rdi = 0
  end
  continue
end
continue
```

This example gdb script demonstrates how you can automatically break on system calls, and how you can use conditions within your commands to conditionally perform gdb commands.

In the previous level, your gdb scripting solution likely still required you to copy and paste your solutions.
This time, try to write a script that doesn't require you to ever talk to the program, and instead automatically solves each challenge by correctly modifying registers / memory.

----
**RELEVANT DOCUMENTATION:**
- gdb's [run](https://sourceware.org/gdb/current/onlinedocs/gdb#Starting) command
- gdb's [continue](https://sourceware.org/gdb/current/onlinedocs/gdb#Continuing-and-Stepping) command
- gdb's [info](https://sourceware.org/gdb/current/onlinedocs/gdb#Registers) command
- gdb's [print](https://sourceware.org/gdb/current/onlinedocs/gdb#Data) command
- gdb's [examine](https://sourceware.org/gdb/current/onlinedocs/gdb#Memory) command
- gdb's [break](https://sourceware.org/gdb/current/onlinedocs/gdb#Set-Breaks) command
- gdb's [display](https://sourceware.org/gdb/current/onlinedocs/gdb#Auto-Display) command
- gdb's [various stepping commands](https://sourceware.org/gdb/current/onlinedocs/gdb#Continuing-and-Stepping) command (that whole section)
- gdb's [breakpoint scripting](https://sourceware.org/gdb/current/onlinedocs/gdb#Break-Commands)
- gdb's [set](https://sourceware.org/gdb/current/onlinedocs/gdb#Assignment) command. Keep in mind that, in this challenge, you'll specifically use this command to set registers (e.g., `$rdi` as above) and memory (as described at the bottom of the linked section).

---

#### Solution

Tương tự như cấp độ trước nhưng cấp độ này nó yêu cầu mình viết script tự động luôn việc nhập giá trị random đó và 1 lưu ý nữa là trong gdb mình có thể change giá trị trong bộ nhớ hay thanh ghi. Vì thế bài này, mình sẽ đặt breakpoint ngay trước khi nó so sánh 2 giá trị input và giá trị target (random). Sau đó khi nhảy tới thì mình sẽ change 2 giá trị đó thành 0 để khi so sánh thì nó bằng nhau. Vì vậy sau khi chạy cùng với script thì mình chỉ cần spam vào input cái gì thì nó cũng pass.

```shell
start
break *main+686
continue
commands
  set $rax = 0
  set $rdx = 0
  continue
end
continue
```


    challenge by correctly modifying registers / memory.


    Program received signal SIGTRAP, Trace/breakpoint trap.
    0x000058c7babe0caf in main ()
    The random value has been set!

    Random value: a
    You input: a
    The correct answer is: 59a2a720c5479cc1

    Breakpoint 2, 0x000058c7babe0d54 in main ()
    The random value has been set!

    Random value: a
    You input: a
    The correct answer is: 98119f4a7dd2368e

    Breakpoint 2, 0x000058c7babe0d54 in main ()
    The random value has been set!

    Random value: a
    You input: a
    The correct answer is: a935fdce97df99e

    ...

    Breakpoint 2, 0x000058c7babe0d54 in main ()
    The random value has been set!

    Random value: You input: a
    The correct answer is: 4edba32af5ad3f84

    Breakpoint 2, 0x000058c7babe0d54 in main ()
    The random value has been set!

    Random value: You input: a
    The correct answer is: bb7606f761707c0e

    Breakpoint 2, 0x000058c7babe0d54 in main ()
    You win! Here is your flag:
    pwn.college{It2lgE4imx-0E2xLnnxpqT7CfX8.dlDNywCMxADNwEzW}

---

#### Flag
    pwn.college{It2lgE4imx-0E2xLnnxpqT7CfX8.dlDNywCMxADNwEzW}

---

### Level 7 - Modifying Execution

---

This level will expose you to some of the true power of gdb.

----
**RELEVANT DOCUMENTATION:**
- gdb's [run](https://sourceware.org/gdb/current/onlinedocs/gdb#Starting) command
- gdb's [continue](https://sourceware.org/gdb/current/onlinedocs/gdb#Continuing-and-Stepping) command
- gdb's [info](https://sourceware.org/gdb/current/onlinedocs/gdb#Registers) command
- gdb's [print](https://sourceware.org/gdb/current/onlinedocs/gdb#Data) command
- gdb's [examine](https://sourceware.org/gdb/current/onlinedocs/gdb#Memory) command
- gdb's [break](https://sourceware.org/gdb/current/onlinedocs/gdb#Set-Breaks) command
- gdb's [display](https://sourceware.org/gdb/current/onlinedocs/gdb#Auto-Display) command
- gdb's [various stepping commands](https://sourceware.org/gdb/current/onlinedocs/gdb#Continuing-and-Stepping) command (that whole section)
- gdb's [breakpoint scripting](https://sourceware.org/gdb/current/onlinedocs/gdb#Break-Commands)
- gdb's [set](https://sourceware.org/gdb/current/onlinedocs/gdb#Assignment) command
- gdb's [call](https://sourceware.org/gdb/current/onlinedocs/gdb#Calling) command. Keep in mind that the syntax for the expression is similar to C's syntax.

---

#### Solution

Cấp độ này yêu cầu mình `call` hàm `win` (trong info khi `run` gdb). Nó báo là trong tất cả các level từ đầu tới giờ ta chỉ cần run hàm đó là xong :). Vì khi ta đang ở trong trình debug ta có truyền sửa và khám phá bất cứ thứ gì về file đó.

    hacker@debugging-refresher~modifying-execution:/challenge$ ./embryogdb_level7 
    The program is restarting under the control of gdb! You can run the program with the gdb command `run`.

    GNU gdb (Ubuntu 9.2-0ubuntu1~20.04.2) 9.2
    Copyright (C) 2020 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.
    Type "show copying" and "show warranty" for details.
    This GDB was configured as "x86_64-linux-gnu".
    Type "show configuration" for configuration details.
    For bug reporting instructions, please see:
    <http://www.gnu.org/software/gdb/bugs/>.
    Find the GDB manual and other documentation resources online at:
        <http://www.gnu.org/software/gdb/documentation/>.

    For help, type "help".
    Type "apropos word" to search for commands related to "word"...
    Reading symbols from /challenge/embryogdb_level7...
    (No debugging symbols found in /challenge/embryogdb_level7)
    (gdb) start
    Temporary breakpoint 1 at 0x1a86
    Starting program: /challenge/embryogdb_level7 

    Temporary breakpoint 1, 0x000060478bf77a86 in main ()
    (gdb) r
    The program being debugged has been started already.
    Start it from the beginning? (y or n) y
    Starting program: /challenge/embryogdb_level7 
    ###
    ### Welcome to /challenge/embryogdb_level7!
    ###

    GDB is a very powerful dynamic analysis tool which you can use in order to understand the state of a program throughout
    its execution. You will become familiar with some of gdb's capabilities in this module.

    As we demonstrated in the previous level, gdb has FULL control over the target process. Under normal circumstances, gdb
    running as your regular user cannot attach to a privileged process. This is why gdb isn't a massive security issue which
    would allow you to just immediately solve all the levels. Nevertheless, gdb is still an extremely powerful tool.

    Running within this elevated instance of gdb gives you elevated control over the entire system. To clearly demonstrate
    this, see what happens when you run the command `call (void)win()`. As it turns out, all of the levels in this module
    can be solved in this way.

    GDB is very powerful!


    Program received signal SIGTRAP, Trace/breakpoint trap.
    0x00005a91ae71bbb7 in main ()
    (gdb) call (void)win()
    You win! Here is your flag:
    pwn.college{0OkWDvyc2CZTipy5oZF-6KyZYQv.dBTNywCMxADNwEzW}


    (gdb) 

---

#### Flag
    pwn.college{0OkWDvyc2CZTipy5oZF-6KyZYQv.dBTNywCMxADNwEzW}

---

### Level 8 - Broken Functions

The previous level showed you raw, but unrefined power.
This level will force you to refine it, as the `win` function will no longer work.
`break` at it, look around, and understand what is wrong.

----
**RELEVANT DOCUMENTATION:**
- gdb's [run](https://sourceware.org/gdb/current/onlinedocs/gdb#Starting) command
- gdb's [continue](https://sourceware.org/gdb/current/onlinedocs/gdb#Continuing-and-Stepping) command
- gdb's [info](https://sourceware.org/gdb/current/onlinedocs/gdb#Registers) command
- gdb's [print](https://sourceware.org/gdb/current/onlinedocs/gdb#Data) command
- gdb's [examine](https://sourceware.org/gdb/current/onlinedocs/gdb#Memory) command
- gdb's [break](https://sourceware.org/gdb/current/onlinedocs/gdb#Set-Breaks) command
- gdb's [display](https://sourceware.org/gdb/current/onlinedocs/gdb#Auto-Display) command
- gdb's [various stepping commands](https://sourceware.org/gdb/current/onlinedocs/gdb#Continuing-and-Stepping) command (that whole section)
- gdb's [breakpoint scripting](https://sourceware.org/gdb/current/onlinedocs/gdb#Break-Commands)
- gdb's [set](https://sourceware.org/gdb/current/onlinedocs/gdb#Assignment) command
- gdb's [call](https://sourceware.org/gdb/current/onlinedocs/gdb#Calling) command
- gdb's [jump](https://sourceware.org/gdb/current/onlinedocs/gdb#Jumping) command

---

#### Solution

Đối với cấp độ này nó yêu cầu mình khám và hàm win, vì có lẽ hàm win đã bị hỏng. Vì thế mình đọc qua mã của hàm win và đặt thanh ghi `rip` vào địa chỉ của lệnh nào đó để sau khi next lệnh đó thì nó có thể get được flag.

Và khi xem qua thì mình thấy ngay đoạn này:

    0x00005aea1912296b <+26>:    lea    0x1(%rax),%edx
    0x00005aea1912296e <+29>:    mov    -0x8(%rbp),%rax
    0x00005aea19122972 <+33>:    mov    %edx,(%rax)
    0x00005aea19122974 <+35>:    lea    0x73e(%rip),%rdi        # 0x5aea191230b9
    0x00005aea1912297b <+42>:    callq  0x5aea19122180 <puts@plt>
    0x00005aea19122980 <+47>:    mov    $0x0,%esi
    0x00005aea19122985 <+52>:    lea    0x749(%rip),%rdi        # 0x5aea191230d5
    0x00005aea1912298c <+59>:    mov    $0x0,%eax

Có `0x5aea191230b9` khi chuyển sang string thì có nghĩa là `You win! Here is your flag:`. Vì thế mình sẽ đặt `rip` tại điểm này sau đó continue là get được flag.



    Program received signal SIGTRAP, Trace/breakpoint trap.
    0x000058e54267db99 in main ()
    (gdb) set $rip=*win+35
    (gdb) c
    Continuing.
    You win! Here is your flag:
    pwn.college{U9uMa6yVypir9God2FkPtcIfu4U.QX5MzMzwCMxADNwEzW}

---

#### Flag

    pwn.college{U9uMa6yVypir9God2FkPtcIfu4U.QX5MzMzwCMxADNwEzW}

---

See yaa!!!