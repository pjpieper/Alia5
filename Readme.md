# Project Alia5 - C0D3
-----------------------------------<img src="https://i.imgur.com/Bfi6vAU.png" alt="drawing" width="400"/></div>------------------------------------

This is a project intended to be displayed for the Kennesaw State University CPE 4850 Senior Design course. 

## What is Alia5?
Technology expands at a rapid pace, far beyond a government's control to properly regulate it. Compounding that issue is when government gets hold of said technology and uses it without truly understanding the consequences that entails. One such technology that threatens the ability for people to express their discontent or exercise their rights in a democracy is facial recognition software and technology.

Alia5 (pronounced Alias) is our attempt at rectifying some of the issues with facial recognition technology that society faces today, both within the United States and abroad, such as in China or the European Union. Using an onboard IR LED array, an embedded system utilizing a Raspberry Pi, a small but powerful rechargeable power bank, and a camera, we intend to give people the tools to counteract facial recognition software.

## How does it work?
![](final_623a80df93b86e00a3956ac1_818240.gif)
Alia5 uses IR LEDs to add input to cameras to confuse facial recognition software and facial mapping techniques. Facial recognition technology as well as facial mapping primarily use deep neural networks to identify individuals. Based on research (Source: https://arxiv.org/abs/1710.08864), even something as simple as a one pixel attack can defeat a wide array of recognition algorithms. Using this fact moving forward, our goal is to exploit this weakness, where the result is highly input dependent, by changing the input just enough to defeat facial recognition.

# Files
Most the files required are included within this repository.

## Dependencies
* TKinter
* PyQT5
