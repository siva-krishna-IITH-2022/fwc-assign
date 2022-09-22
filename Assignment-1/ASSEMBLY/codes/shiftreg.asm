.include "/home/krishna/gcc/codes/m328Pdef.inc"
ldi r16,0b00100000
out DDRB,r16

ldi r16,0b00100000
out PortB,r16
call wait

ldi r16,0b00000000
out PortB,r16
call wait

wait:
  push r16		;save register contents
  push r17		
  push r18		

  ldi r16, 0x90		;loop 0x400000 times
  ldi r17, 0x20		;12 million cycles
  ldi r18, 0x20		;0.7s at 16 MHz

w0:
  
  dec r18
  brne w0
  dec r17
  brne w0
  dec r16
  brne w0

  pop r18		;restore register contents
  pop r17	
  pop r16
  

  ret
  
  
Start:
  rjmp Start
