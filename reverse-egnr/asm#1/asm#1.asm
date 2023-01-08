; text for the actual code
section .text:
	global _start
_start: 
	main:
        push    rbp
        mov     rbp, rsp
        mov     DWORD PTR [rbp-4], 10
        add     DWORD PTR [rbp-4], 50
        sub     DWORD PTR [rbp-4], 100
        add     DWORD PTR [rbp-4], 1328
        mov     eax, DWORD PTR [rbp-4]
        pop     rbp
        ret

; data is for declaring initialized data or constant
section .data:



; bss section is for declaring variable
section .bss:
