# Outline

-   What is a Microcontroller?

-   Microcontroller vs. Computers / Single Board Computers (OS systems)

    -   Discuss bare-metal

-   Microcontroller platforms

    -   Arduino vs. Raspberry Pi Pico vs. STM 32

-   Micropython vs. C

-   Software Setup

    -   Install Thonny + Flash Pico

-   Hands-on Tutorial

    -   Electronic Basics

        -   Ohms law - calculate resistor

    -   Wire up and blink the LED

    -   Add button control

    -   Reaction timer - Who has the fastest reaction time!

    -   If time allows:

        -   Button interrupt

        -   PWM

        -   Read from the photoresistor

        -   Ambient light program (adjust PWM based on photoresistor
            value)

# Workshop![](media/image3.png){width="6.177083333333333in" height="2.5152001312335956in"}

## What is a Microcontroller?

**Microcontroller/ microcontroller unit (MCU):** a small
[[computer]{.underline}](https://en.wikipedia.org/wiki/Computer) on a
single [[integrated
circuit]{.underline}](https://en.wikipedia.org/wiki/Integrated_circuit),
designed for embedded applications.

-   [generally designed to run a single basic programme
    repeatedly]{.mark}

### What are the elements of a microcontroller?

The core elements that make up a microcontroller are the central
processing unit (CPU), memory and I/O peripherals.

1.  CPU (microprocessor): the brain of the device. It processes and
    responds to various instructions that direct the microcontroller\'s
    function. This involves performing basic arithmetic, logic and I/O
    operations. It also performs data transfer operations, which
    communicate commands to other components in the larger embedded
    system.

2.  Memory: A microcontroller\'s memory stores the data that the
    processor receives and uses to respond to instructions it\'s
    programmed to carry out. A microcontroller has two main memory
    types:

    i.  Program memory: This stores long-term information about the
        instructions that the CPU carries out. Program memory is
        non-volatile memory, meaning it stores information over time
        without needing a power supply.

    ii. Data memory: This temporary data storage is used while the
        instructions are being executed. Data memory is volatile,
        meaning the data it holds is temporary and is only maintained if
        the device is connected to a power source.

3.  I/O peripherals: The I/O devices are the interface for the processor
    to the outside world. The input ports receive information and send
    it to the processor in the form of
    [[binary]{.underline}](https://www.techtarget.com/whatis/definition/binary)
    data. The processor receives that data and sends the necessary
    instructions to output devices, which execute tasks external to the
    microcontroller.

4.  Other elements: While the processor, memory and I/O peripherals are
    the defining elements of the microprocessor, there are other
    elements that are frequently included. The term I/O peripheral
    refers to a supporting component that interfaces with the memory and
    processor. There are many supporting components that can be
    classified as peripherals. Having some manifestation of an I/O
    peripheral is elemental to a microprocessor because it is the
    mechanism through which the processor functions. Other supporting
    elements of a microcontroller include the following:

-   Analog-to-digital converter. An
    [[ADC]{.underline}](https://www.techtarget.com/whatis/definition/analog-to-digital-conversion-ADC)
    is a circuit that converts analog signals to digital signals. It
    lets the processor at the center of the microcontroller interface
    with external analog devices, such as sensors.

-   Digital-to-analog converter. A DAC performs the inverse function of
    an ADC, letting the microcontroller\'s processor communicate its
    outgoing signals to external analog components.

-   System bus. The system bus is the connective wire that links
    together all components of the microcontroller.

-   Serial port. The serial port is one example of an I/O port that
    enables the microcontroller to connect to external components. It
    has a similar function to a
    [[USB]{.underline}](https://www.techtarget.com/whatis/feature/The-history-of-USB-What-you-need-to-know)
    or a parallel port but differs in the way it exchanges bits.

Sources:

-   [[https://en.wikipedia.org/wiki/Microcontroller]{.underline}](https://en.wikipedia.org/wiki/Microcontroller)

-   [[https://au.rs-online.com/web/content/discovery/ideas-and-advice/microcontrollers-guide?srsltid=AfmBOookUBi_7Yf4iJbHPFz-ssK2CkOGn3CM_JZ0OLAkNIL7nLM_ijqb]{.underline}](https://au.rs-online.com/web/content/discovery/ideas-and-advice/microcontrollers-guide?srsltid=AfmBOookUBi_7Yf4iJbHPFz-ssK2CkOGn3CM_JZ0OLAkNIL7nLM_ijqb)

-   [[https://www.techtarget.com/iotagenda/definition/microcontroller]{.underline}](https://www.techtarget.com/iotagenda/definition/microcontroller)

## Microcontroller vs. Computers (OS systems) vs. Single Board Computers (OS systems)

  ------------------------------------------------------------------------
  **Microprocessor (MPU)** **Microcontroller      **Single Board Computer
                           (MCU)**                (SBC)**
  ------------------------ ---------------------- ------------------------
  The heart of a computer  The heart of an        Microcomputer
  system                   embedded system        

  Memory and I/O           Has an external        Has an external
  components has to be     component with an      component with an
  connected externally     internal memory and    internal memory and I/O
                           I/O components         components

  Unable to use in compact Able to use in compact Able to use in compact
  systems                  system                 system

  Cost of the system is    Cost of the system is  Cost of the system is
  higher                   lower                  lower

  Since memory and I/O     Components are         Components are internal,
  components are external, internal, where the    where the operation
  each instruction goes    operation takes place  takes place internally,
  through the external     internally, thus it's  thus it's faster
  operation. Thus it's     faster                 
  slower.                                         

  Widely used in PC and    Widely used in small   Widely used in
  laptops, big control     control systems        programming and small
  systems                                         control systems
  ------------------------------------------------------------------------

+-----------------+-----------------+--------------------+-------------+
|                 | MCU →           | SBC                | Computers   |
|                 | bare-metal      |                    |             |
+=================+=================+====================+=============+
| Examples        | [Arduino,       | [Raspberry Pi,     | Laptop,     |
|                 | ESP32,          | BeagleBone, NVIDIA | Desktop PC  |
|                 | Raspberry Pi    | Jetson             |             |
|                 | Pico,           | Nano]{.mark}       |             |
|                 | STM32]{.mark}   |                    |             |
+-----------------+-----------------+--------------------+-------------+
| Processing      | [Designed for   | [Much more         | Full        |
| power           | simple,         | powerful, capable  | gene        |
|                 | dedicated       | of handling        | ral-purpose |
|                 | tasks.          | complex operations | computing.  |
|                 | Processing      | and                | Very high,  |
|                 | capability is   | mul                | designed    |
|                 | low but highly  | titasking.]{.mark} | for complex |
|                 | optimized for   |                    | a           |
|                 | effi            |                    | pplications |
|                 | ciency.]{.mark} |                    |             |
+-----------------+-----------------+--------------------+-------------+
| Memory &        | [Very limited   | [Offers            | Several     |
| storage         | resources,      | significantly more | GB--TB +    |
|                 | typically       | memory and         | storage:    |
|                 | measured in     | storage, often in  | SSD/HDD     |
|                 | kilobytes (KB)  | gigabytes (GB),    | (hundreds   |
|                 | or a few        | suitable for       | of GB or    |
|                 | megabytes       | running full       | TB)         |
|                 | (MB).]{.mark}   | app                |             |
|                 |                 | lications.]{.mark} |             |
+-----------------+-----------------+--------------------+-------------+
| Operating       | [Usually runs   | [Supports full     | Runs full   |
| system          | without an      | operating systems  | OS          |
|                 | operating       | like Linux,        | (Windows,   |
|                 | system or uses  | enabling a wide    | macOS,      |
|                 | minimal         | range of software  | Linux)      |
|                 | firmware for    | and tools.]{.mark} |             |
|                 | basic control.  |                    |             |
|                 | →               |                    |             |
|                 | bar             |                    |             |
|                 | e-metal]{.mark} |                    |             |
+-----------------+-----------------+--------------------+-------------+
| Power           | [Extremely low  | [Higher power draw | High        |
| consumption     | power           | and requires a     | (ten        |
|                 | requirements,   | stable power       | s--hundreds |
|                 | ideal for       | source for         | of W)       |
|                 | battery-powered | reliable           |             |
|                 | or              | operation.]{.mark} |             |
|                 | e               |                    |             |
|                 | nergy-sensitive |                    |             |
|                 | d               |                    |             |
|                 | evices.]{.mark} |                    |             |
+-----------------+-----------------+--------------------+-------------+
| Cost            | [Very           | [More expensive,   | Much more   |
|                 | affordable,     | starting around    | expensive   |
|                 | typically       | £30 and going well |             |
|                 | priced between  | over £100          |             |
|                 | £2 and          | depending on       |             |
|                 | £20.]{.mark}    | speci              |             |
|                 |                 | fications.]{.mark} |             |
+-----------------+-----------------+--------------------+-------------+
| Pros            | [- Extremely    | [- Powerful        |             |
|                 | low power       | processing and     |             |
|                 | cons            | mu                 |             |
|                 | umption]{.mark} | ltitasking]{.mark} |             |
|                 |                 |                    |             |
|                 | [- Affordable   | [- Runs full       |             |
|                 | and widely      | operating          |             |
|                 | av              | systems]{.mark}    |             |
|                 | ailable]{.mark} |                    |             |
|                 |                 | [- Ideal for       |             |
|                 | [- Great for    | networking and     |             |
|                 | real-time       | advanced           |             |
|                 | control and     | projects]{.mark}   |             |
|                 | simple          |                    |             |
|                 | tasks]{.mark}   |                    |             |
+-----------------+-----------------+--------------------+-------------+
| Cons            | [- Limited      | [- Higher power    |             |
|                 | processing      | re                 |             |
|                 | power]{.mark}   | quirements]{.mark} |             |
|                 |                 |                    |             |
|                 | [- No operating | [- More            |             |
|                 | system]{.mark}  | expensive]{.mark}  |             |
|                 |                 |                    |             |
|                 | [- Not suitable | [- Overkill for    |             |
|                 | for complex     | simple             |             |
|                 | appli           | tasks]{.mark}      |             |
|                 | cations]{.mark} |                    |             |
+-----------------+-----------------+--------------------+-------------+

Bare Metal Concept: eliminates the intermediary layers of operating
systems, allowing developers to interact directly with the hardware.

-   Pros:

    -   Maximizes Resource Utilization by eliminating OS overhead

    -   Predictable performance - good for applications with precise
        timing

    -   Reduced Complexity - removes the need to navigate the OS

-   Cons:

    -   Limited abstraction - have to deal with hardware-specific
        details

    -   Portability challenges - program tied to hardware architecture

    -   No standardization

Sources:

-   [[https://www.rapidonline.com/news/microcontrollers-vs-sbcs]{.underline}](https://www.rapidonline.com/news/microcontrollers-vs-sbcs)

-   [[https://www.seeedstudio.com/blog/2020/10/27/all-about-cpus-microprocessor-microcontroller-and-single-board-computer/?srsltid=AfmBOoqtRTSdS8Ib6V3vWTlOloNbQ5Vt6UJ1i5RjFDlSY1ZcepArs1gi]{.underline}](https://www.seeedstudio.com/blog/2020/10/27/all-about-cpus-microprocessor-microcontroller-and-single-board-computer/?srsltid=AfmBOoqtRTSdS8Ib6V3vWTlOloNbQ5Vt6UJ1i5RjFDlSY1ZcepArs1gi)

-   [[https://intechhouse.com/blog/what-is-bare-metal-programming-in-embedded-system/]{.underline}](https://intechhouse.com/blog/what-is-bare-metal-programming-in-embedded-system/)
    (bare metal)

## Microcontroller platforms

-   [[Arduino
    boards]{.underline}](https://www.rapidonline.com/brands/arduino?Attributes=%7B%22T3%22:%5B%22Arduino+Breakout+%26+Boards%22%5D%7D&shoppingmode=true)
    (ATmega series) - Popular among hobbyists and makers, Arduino boards
    use ATmega microcontrollers. They're easy to program, have a large
    community and are ideal for prototyping projects like
    [[robotics]{.underline}](https://www.rapidonline.com/research-robotics),
    IoT devices and automation.

-   **Raspberry Pi Pico (RP2040)** -- The Pico uses the RP2040
    microcontroller developed by Raspberry Pi. It's inexpensive,
    powerful, and supports both MicroPython and C/C++. It's commonly
    used for embedded learning, robotics, and sensor-based projects.

-   [[PIC
    microcontrollers]{.underline}](https://www.rapidonline.com/pic-microcontrollers) -
    Produced by Microchip Technology, PIC microcontrollers are known for
    their reliability and versatility. They're widely used in industrial
    control systems, consumer electronics and automotive applications.

-   [[STM32
    series]{.underline}](https://www.rapidonline.com/stmicroelectronics-conrad-pcb-design-board-659563-659563) -
    Based on ARM Cortex cores, STM32 microcontrollers offer high
    performance and low power consumption. They're commonly used in
    advanced applications like medical devices, drones and complex
    embedded systems.

### Raspberry Pi Pico versions:

H - extensions just means that the pins are already soldered

+-----------------+-----------------+-----------------+-----------------+
| Pico            | Pico W ← were   | Pico 2          | Pico 2 W        |
|                 | using this      |                 |                 |
+=================+=================+=================+=================+
| \- RP2040       | Pico +          | Pico + improved | Pico 2 +        |
| microcontroller |                 | performance:    |                 |
|                 | \- 2.4 GHz      |                 | \- RP2350       |
| \- Dual-core    | Wi-Fi           | \- dual         | microcontroller |
| ARM Cortex-M0+  |                 | **Cortex-M33    |                 |
|                 | \- Bluetooth    | cores** (or     | \- Wi-Fi        |
| \- 133 MHz CPU  | support         | RISC-V cores)   | 802.11n         |
|                 |                 |                 |                 |
| \- 264 KB SRAM  | \- Infineon     | **- 150 MHz     | \- Bluetooth    |
|                 | CYW43439 radio  | clock**         | 5.2             |
| \- 2 MB flash   | chip            |                 |                 |
|                 |                 | **- 520 KB RAM  | \- same pinout  |
| \- 26 GPIO pins |                 | (≈2× more)**    | as previous     |
|                 |                 |                 | Pico boards     |
| \- ADC, PWM,    |                 | **- 4 MB        |                 |
| I²C, SPI, UART  |                 | flash**         |                 |
|                 |                 |                 |                 |
|                 |                 | \- more PWM and |                 |
|                 |                 | PIO capability  |                 |
|                 |                 |                 |                 |
|                 |                 | \- improved     |                 |
|                 |                 | security        |                 |
|                 |                 | (TrustZone)     |                 |
+-----------------+-----------------+-----------------+-----------------+
| \- basic        | \- IoT          |                 | \- IoT devices  |
| embedded        |                 |                 |                 |
| learning        | \- web servers  |                 | \- wireless     |
|                 |                 |                 | robotics        |
| \- robotics     | \- wireless     |                 |                 |
|                 | sensors         |                 | \-              |
| \- sensor       |                 |                 | cloud-connected |
| projects        |                 |                 | sensors         |
+-----------------+-----------------+-----------------+-----------------+

  ---------------------------------------------------------------------------------------
  **Board**   **MCU**   **CPU**                      **RAM**   **Flash**   **Wireless**
  ----------- --------- ---------------------------- --------- ----------- --------------
  Pico        RP2040    Dual ARM Cortex-M0+ \@133    264 KB    2 MB        ❌
                        MHz                                                

  Pico W      RP2040    Dual ARM Cortex-M0+ \@133    264 KB    2 MB        Wi-Fi +
                        MHz                                                Bluetooth

  Pico 2      RP2350    Dual Cortex-M33 **or**       520 KB    4 MB        ❌
                        RISC-V \@150 MHz                                   

  Pico 2 W    RP2350    Dual Cortex-M33 **or**       520 KB    4 MB        Wi-Fi +
                        RISC-V \@150 MHz                                   Bluetooth
  ---------------------------------------------------------------------------------------

![](images/pico-img.png){width="3.48379593175853in"
height="1.6666305774278216in"}![](images/pico-2-img.png){width="3.460648512685914in"
height="1.648386920384952in"}

Sources:

-   [[https://www.rapidonline.com/news/microcontrollers-vs-sbcs]{.underline}](https://www.rapidonline.com/news/microcontrollers-vs-sbcs)

-   [[https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html]{.underline}](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)

## Micropython vs. C

  ------------------------------------------------------------------------
  Feature         MicroPython                 C/C++ (Pico SDK)
  --------------- --------------------------- ----------------------------
  Ease of Use     High (Interpreted, REPL     Moderate (Requires
                  support)                    compilation)

  Setup Time      Fast (Drag & drop UF2)      Slower (CMake, Toolchains)

  Performance     Sufficient for most DIY/IoT Maximum (up to 250x faster)

  Control         High-level abstraction      Direct register/hardware
                                              access

  Debugging       Print statements / REPL     SWD / Debug probes / GDB
  ------------------------------------------------------------------------

##  

## Software Setup![](media/image7.png){width="3.0208333333333335in" height="2.8226159230096237in"}

1.  Install Thonny IDE from:
    [[https://thonny.org/]{.underline}](https://thonny.org/)

2.  Open Thonny, go to tools→ options → Interpretter

3.  Select Micropython (Raspberry Pi Pico)

4.  Hold the BOOTSEL button

5.  Plug the Pico into USB.

6.  Flash with Thonny

> ![](micropython_setup_screenshots/pico_as_drive.png){width="2.925300743657043in"
> height="1.7048928258967628in"}![](micropython_setup_screenshots/select_micropython.png){width="3.0208333333333335in"
> height="1.762684820647419in"}![](micropython_setup_screenshots/install_micropython.png){width="3.375in"
> height="1.972402668416448in"}

-   Or can Drag the [[MicroPython .uf2
    file]{.underline}](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
    onto the RPI-RP2 drive manually

7.  The Pico reboots.

8.  Run the following to flash the onboard LED:

> ![](micropython_setup_screenshots/blink.png){width="4.125in" height="2.6843985126859145in"}


## Electronic Basics

-   Ohms law - calculate resistor

## Hands-on Tutorial


-   Wire up and blink LED

-   Add button control

-   Reaction timer - Who has the fastest reaction time!

-   If time allow:

    -   Button interrupt

    -   PWM

    -   Read from photoresistor

    -   Ambient light program (adjust PWM based on photoresistor value)
