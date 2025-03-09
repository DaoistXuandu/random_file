flag_list = {
  "N",
  "T",
  "O",
  "E",
  "S",
  "}",
  "{"
}

function checkFlag()
  io.write("What's index number 0? ")
  a = io.read()
  if a == flag_list[1] then
    io.write("What's index number 1? ")
    a = io.read()
    if a == flag_list[4] then
      io.write("What's index number 2? ")
      a = io.read()
      if a == flag_list[2] then
        io.write("What's index number 3? ")
        a = io.read()
        if a == flag_list[5] then
          io.write("What's index number 4? ")
          a = io.read()
          if a == flag_list[3] then
            io.write("What's index number 5? ")
            a = io.read()
            if a == flag_list[5] then
              io.write("What's index number 6? ")
              a = io.read()
              if a == flag_list[7] then
                io.write("What's index number 7? ")
                a = io.read()
                if a == string.char(string.byte(flag_list[3]) - 3) then
                  io.write("What's index number 8? ")
                  a = io.read()
                  if a == string.char(tonumber(string.format("%X", string.byte(flag_list[4]) + 16), 16)) then
                    io.write("What's index number 9? ")
                    a = io.read()
                    if a == string.char(string.byte(flag_list[5]) % 78 * 13) then
                      io.write("What's index number 10? ")
                      a = io.read()
                      if a == string.char(string.byte(flag_list[1]) % 78 + 114) then
                        io.write("What's index number 11? ")
                        a = io.read()
                        if a == string.char(95) then
                          io.write("Last Input: ")
                          a = io.read()
                          if a == string.lower(string.format("%X", 832717073)) then
                            print("REDACTED Congrats")
                          else
                            print("False")
                          end
                        else
                          print("False")
                        end
                      else
                        print("False")
                      end
                    else
                      print("False")
                    end
                  else
                    print("False")
                  end
                else
                  print("False")
                end
              else
                print("False")
              end
            else
              print("False")
            end
          else
            print("False")
          end
        else
          print("False")
        end
      else
        print("False")
      end
    else
      print("False")
    end
  else
    print("False")
  end
end

checkFlag()
