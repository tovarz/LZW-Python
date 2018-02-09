from hash_table import hash_table

def encode(in_file, table):
    s = ""
    holder = ""
    out_string = ""
    while in_file != "":
        k = in_file[0]
        main_string = holder + k
        if(table.find(main_string) != None):
            holder = main_string
        else:
            table.insert(main_string)
            p = table.return_code(holder)
            out_string = out_string + p 
            out_string = out_string + " "
            holder = k

    return out_string
def main():
    table = hash_table()
    print("Enter file name:")
    file_name = input()

    f_in = open(file_name, "r")
    f_out = open("compressed_" + file_name, "w")

    in_file = f_in.read()
    for i in range(1, 256):
        table.insert(chr(i))
    
    out_string = encode(in_file,table)
    print("Encode is finished.")
    f_out.write(out_string)

if __name__ == "__main__":
    main()