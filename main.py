row = ['1','2','3','4','5','6','7','8'];
column = ['a','b','c','d','e','f','g','h'];
pieces = ['R','N','B','Q','K'];

def is_piece(x):
    if x in pieces:
        return True;
    else:
        return False;

def is_piece_other_than_king(x):
    if x in pieces[0:-1]:
        return True;
    else:
        return False;

def is_row(x):
    if x in row:
        return True;
    else:
        return False;

def is_column(x):
    if x in column:
        return True;
    else:
        return False;

def is_round(x):
    """Returns True if given string is a round of chess"""
    if x == '':
        return False;
    if x == 'O-O-O' or x == 'O-O':
        return True;
    if x == '1-0' or x == '0-1' or x == '0-0':
        return True;

    if x[-1] == '+' or x[-1] == '#':
        x = x.replace('+','');
        x = x.replace('#','');

    if x[-1].isupper() and is_piece_other_than_king(x[-1]) and x[-2] == '=' \
     and is_row(x[-3]) and is_column(x[-4]) and x[-4] == x[0]:
        return True;

    if len(x) == 2:
        if is_column(x[0]) and is_row(x[1]):
            return True;
    elif len(x) == 3:
        if is_piece(x[0]) and is_column(x[1]) and is_row(x[2]):
            return True;
    elif len(x) == 4:
        if is_piece(x[0]) and x[1] =='x' and is_column(x[2]) and is_row(x[3]):
            return True;
        elif is_piece(x[0]) and is_column(x[1]) and is_column(x[2]) and \
        is_row(x[3]):
            return True;
        elif is_column(x[0]) and x[1] =='x' and is_column(x[2]) and is_row(x[3]):
            return True;
    elif len(x) == 5:
        if is_piece(x[0]) and is_column(x[1]) and x[2]=='x' and is_column(x[3])\
        and is_row(x[4]):
            return True;
    else:
        return False;

class Annotation:
    """This class saves chess chess moves
    white_player -> white player name. str
    black_player -> black player name. str"""
    def __init__(self, white_player, black_player):
        """Initialization of the parameters. player names are stored.
        3 additional lists are used to store captured pieces and the moves"""
        self.players = [white_player, black_player];
        self.white_captured_pieces = [0, 0, 0, 0, 0];
        self.black_captured_pieces = [0, 0, 0, 0, 0];
        self.game = ['a2','a7','b2','b7','c2','c7','d2','d7','e2','e7','f2',
            'f7','g2','g7','h2','h7','Ra1','Ra8','Nb1','Nb8','Bc1','Bc8','Qd1',
            'Qd8','Ke1','Ke8','Bf1','Bf8','Ng1','Ng8','Rh1','Rh8'];

    def write_round(self):
        """Prompts the user for the next moves."""
        white_move = str(input("Ingresa la jugada de las blancas ")).strip();
        black_move = str(input("Ingresa la jugada de las negras ")).strip();
        try:
            if is_round(white_move) and is_round(black_move):
                    self.game.append(white_move);
                    self.game.append(black_move);

                    if 'x' in white_move:
                        in_1 = white_move.index('x');
                        self.black_piece_captured(white_move[in_1+1:in_1+3], \
                        self.black_captured_pieces);
                    if 'x' in black_move:
                        in_2 = black_move.index('x');
                        self.white_piece_captured(black_move[in_2+1:in_2+3], \
                        self.white_captured_pieces);
            else:
                print("Notación inválida. Por favor, intente nuevamente.");
                self.write_round();
        except:
            print("Ha ocurrido un error. Por favor intente nuevamente.")

    def display_game(self):
        """Displays all the rounds up to that point."""
        print('jugadas\n');
        for i in range(17, int((len(self.game)/2)+1)):
            print(f"{i-16}. {self.game[(2*i)-2]} {self.game[(2*i)-1]}");

    def display_round(self):
        """Displays requested n round."""
        try:
            position = int(input("Ingrese la ronda que deseas ver: "));
            assert(position>0);
            position += 16;
            print(f"jugada {position-16}");
            print('jugada blancas: ');
            print(self.game[(2*position)-2]);
            print('jugada negras: ');
            print(self.game[(2*position)-1]);
        except:
            print("Se ha producido un error. Por favor, ingresa un entero en el rango de jugadas");
            self.display_round();

    def display_captured_pieces(self):
        """Displays captured pieces."""
        print('piezas capturadas por el jugador blanco: ');
        print(f"Alfiles: {self.black_captured_pieces[3]}");
        print(f"Caballos: {self.black_captured_pieces[2]}");
        print(f"Damas: {self.black_captured_pieces[4]}");
        print(f"Peones: {self.black_captured_pieces[0]}");
        print(f"Torres: {self.black_captured_pieces[1]}");

        print('piezas capturadas por el jugador negro:');
        print(f"Alfiles: {self.white_captured_pieces[3]}");
        print(f"Caballos: {self.white_captured_pieces[2]}");
        print(f"Damas: {self.white_captured_pieces[4]}");
        print(f"Peones: {self.white_captured_pieces[0]}");
        print(f"Torres: {self.white_captured_pieces[1]}");

    def modify_round(self):
        """Prompts the user to select a round to change."""
        try:
            ronda = int(input("Ingresa la ronda que deseas modificar "));
            assert(ronda>0);
            ronda += 16;
            white_move = str(input("Editando posición de las blancas ")).strip();
            black_move = str(input("Editando posición de las negras ")).strip();
            if is_round(white_move) and is_round(black_move):
                self.game[(2*ronda)-2] = white_move;
                self.game[(2*ronda)-1] = black_move;
                self.display_game();
            else:
                print('Por favor, ingresa jugadas válidas');
                self.modify_round();
        except:
            print('Por favor ingrese un número entero en el rango de jugadas');
            self.modify_round();

    def remove_round(self):
        """Deletes n round."""
        try:
            ronda = int(input("Ingresa la ronda que deseas eliminar "));
            assert(ronda>0);
            ronda += 16;
            self.game.pop((2*(ronda-0))-2);
            self.game.pop((2*(ronda-0))-2);
            self.display_game();
        except:
            print('Se ha producido un error. Por favor, ingresa un entero en el rango de jugadas.');
            self.remove_round();

    def add_round(self):
        """Adds a round anywhere in the rounds."""
        try:
            ronda = int(input("Ingresa el número de la ronda que deseas agregar "));
            assert(ronda>0);
            ronda += 16;
            white_move = str(input("Ingresa la jugada de las blancas ")).strip();
            black_move = str(input("Ingresa la jugada de las negras ")).strip();
            if is_round(white_move) and is_round(black_move):
                self.game.insert((2*(ronda+0))-2, white_move);
                self.game.insert((2*(ronda+0))-1, black_move);
                self.display_game();
            else:
                print('Por favor, ingresa una jugada válida');
                self.add_round();
        except:
            print("Se ha producido un error. Por favor, ingresa un número entero, jugadas válidas dentro del rango.");
            self.add_round();

    def white_piece_captured(self, place, the_list):
        self.capture(len(self.game)-2, place, the_list);

    def black_piece_captured(self, place, the_list):
        self.capture(len(self.game)-3, place, the_list);

    def capture(self, given_index, place, the_list):
        if given_index < 0:
            return None;
        if place in self.game[given_index]:
            if self.game[given_index][0].isupper():
                if self.game[given_index][0] == 'R':
                    the_list[1] += 1;
                    print('se ha capturado una torre');
                elif self.game[given_index][0] == 'N':
                    the_list[2] += 1;
                    print('se ha capturado un caballo')
                elif self.game[given_index][0] == 'B':
                    the_list[3] += 1;
                    print('se ha capturado un alfil')
                elif self.game[given_index][0] == 'Q':
                    the_list[4] += 1;
                    print('se ha capturado una dama');
            else:
                the_list[0] += 1;
                print('se ha capturado un peon');
        else:
            self.capture(given_index-2, place, the_list);

print("Bienvenido a nuestro sistema de anotación");
jugador_blanco = str(input('Ingresa el nombre del jugador con piezas blancas '))
jugador_negro = str(input('Ingresa el nombre del jugador con piezas negras '));
juego = Annotation(jugador_blanco, jugador_negro);
looping = True;
while looping:
    juego.write_round();
    var = str(input('ingresa * para entrar a opciones, presiona enter para seguir anotando jugadas\n'));
    while var == '*':
        print('Lista de comandos:');
        print('\t-d "muestra las jugadas"');
        print('\t-o "muestra una ronda"')
        print('\t-c "muestra las piezas capturadas"');
        print('\t-r "quitar una ronda"');
        print('\t-a "agregar una ronda"');
        print('\t-m "modificar una ronda"');
        print('\tfin "Terminar la partida"');
        print('\tsalir "Regresar a anotar jugadas"');
        var_2 = str(input('Ingresa tu comando \n'));
        if var_2 == '-d':
            juego.display_game();
        elif var_2 == '-o':
            juego.display_round();
        elif var_2 == '-c':
            juego.display_captured_pieces();
        elif var_2 == '-r':
            juego.remove_round();
        elif var_2 == '-a':
            juego.add_round();
        elif var_2 == '-m':
            juego.modify_round();
        elif var_2 == 'fin':
            looping = False;
            break;
        elif var_2 == 'salir':
            var = 'bueans';
        else:
            print('No ingresaste un comando válido.')
print(f"Blancas: {juego.players[0]}");
print(f"Negras: {juego.players[1]}");
juego.display_game();
