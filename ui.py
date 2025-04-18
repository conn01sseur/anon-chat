from config import DEFAULT_HOST, DEFAULT_PORT

def show_banner(host, port):
    banner = f'''
  .  . .  .  . .  .  . .  .  . .  .  . .  .  . .  
   .       .       .       .       .       .     .
     .  .    .  .    .  .    .  .    .  .    .    
 .       .       .       .       .       .     .  
   .  tX%;tt;ttt;;ttt;tt;t;tt;tt;t;tt;tt;t88 .   .
  .   @%;       .                         8:    . 
    . @%;.  .%8%88t88;88;88;88;88;888..   8;  .   
  .   @%;    :S%XS%XS%XS%XS%XS%XS%XX;   . 8:     .
     .@%;. . X.8 8 88@88888888888%888%.   8; . .  
  .   @%;    ;888X88@@88888S88%X88X@8:  . 8;      
   .  @%;.  .S888@888@88888888888@88@. .  8:  .  .
     .@%;    ;SXtXSStSSStX:S%%SSSSX:;    .8;      
 .  . @%;.  . X8888X:.%@888X..t8888X. .   8:  . . 
      @%;    ;88@%88  88SX@8  88@S88::.  .8;      
  .  .@%;.  . X8 .88; 88; 88St8X .t8X.    8;.   . 
   .  @%;   .:X8888X:  888@8;.;8@888t  . .8;  .   
 .    @%;.    ;%%%:.   SS%;;. :t%Stt      8:     .
    . @ .   .8                             X  .   
  .   8@;  .;8:888888:888888888888888:8t8t8.    . 
    . 8X: tX%t.tt%%%t.;t%%%S%%S%S%S%t.:.:  .  .   
  .   @@..8%.   .  .  .  .   .       .   .        
      X8t@;:     .      .       .  .   .    .  .  
  . . % 8@   .      .      .  .      .    .       
      t;@  .   .  .   .  .       .      .    .  . 
  .  .%8                   .  .    .  .    .   .   
         .   .  .  Your host: {host}. . .    .       
  . .      .     . Your port: {port}   .  .  .  .    
      . .     .     .  .     . .      .   .    .  
  .  .    .     .         .      .  .  .     . .  '''

    print(f"""\n{banner}\n
1. Connect (client)
2. Create server
3. Exit\n""")

def get_connection_params():
    host = input(f"Input host [{DEFAULT_HOST}]: ") or DEFAULT_HOST
    port = int(input(f"Input port [{DEFAULT_PORT}]: ") or DEFAULT_PORT)
    key = input("Crypt key: ")
    return host, port, key