def load_prog(filename="prog3.txt"):
    prog = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")
            line_num = int(parts[0].strip())
            cmd_parts = parts[1].strip().split()
            opcode_dec = int(cmd_parts[0])
            arg = int(cmd_parts[1])
            prog[line_num] = (opcode_dec, arg)
    return prog

def load_ram(filename="ram3.txt"):
    ram = [0] * 256
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")
            addr = int(parts[0].strip())
            val = int(parts[1].strip())
            if 0 <= addr < 256:
                ram[addr] = val
    return ram

def print_ram_range(ram, start=0, end=20):
    for i in range(start, end + 1):
        print(f"ram{i} : {ram[i]}")

def run_simulator():
    try:
        prog = load_prog("prog3.txt")
        ram = load_ram("ram3.txt")
    except FileNotFoundError as e:
        print(f"Błąd: Nie znaleziono pliku! ({e.filename})")
        return

    a = 0
    carry = False
    pc = 0
    licznik_krokow = 0
    
    # Wyświetlenie RAM na początku (ram0 - ram20)
    print("=== POCZĄTKOWA ZAWARTOŚĆ RAM (0-20) ===")
    print_ram_range(ram, 0, 20)
    print("=======================================\n")
    
    print("Uruchomienie programu:")
    print("-" * 60)

    while pc in prog:
        opcode, arg = prog[pc]
        
        # Wyświetlenie stanu PRZED pobraniem / wykonaniem opcodu
        print(f"PC: {pc} | Accumulator: {a} | Carry: {carry} ")
        
        # Domyślne ustawienie kolejnego kroku na pc + 1
        next_pc = pc + 1

        if opcode == 0:        # LDA #arg
            a = arg
        elif opcode == 1:      # LDA adresram
            a = ram[arg]
        elif opcode == 2:      # STA adresram
            ram[arg] = a
        elif opcode == 3:      # ADD adresram
            res = (a + ram[arg])
            carry = (res > 255)
            a = res & 0xff
        elif opcode == 4:      # SUB adresram
            val = ram[arg]
            carry = (a < val)
            a = (a - val) & 0xff
        elif opcode == 5:      # LDAA
            a = ram[a]
        elif opcode == 6:      # STAI adresram_zrodlowy
            ram[a] = ram[arg]
        elif opcode == 7:      # JC adresrom
            if carry:
                next_pc = arg
                
        licznik_krokow += 1
        # Przepisanie obliczonego adresu do licznika programu
        pc = next_pc

    print("-" * 60)
    print("Symulacja zakończona.\n")
    
    # Wyświetlenie RAM na końcu (ram0 - ram20)
    print("=== KOŃCOWA ZAWARTOŚĆ RAM (0-20) ===")
    print_ram_range(ram, 0, 20)
    print("=====================================")
    print(f"Wykonano kroków: {licznik_krokow}")

if __name__ == "__main__":
    run_simulator()
