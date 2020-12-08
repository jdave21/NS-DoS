from collections import OrderedDict
exec("".join(map(chr,[int("".join(str(OrderedDict([('A', 0),
             ('B', 1),
             ('C', 2),
             ('D', 3),
             ('E', 4),
             ('F', 5),
             ('G', 6),
             ('H', 7),
             ('I', 8),
             ('J', 9),
             ('K', 10),
             ('1', 11),                                                                       ('2', 12),
             ('3', 13),
             ('4', 14),
             ('5', 15),
             ('6', 16),
             ('7', 17),
             ('8', 18),
             ('9', 19),
             (':)', 20),
             (':/', 21),
             (':{', 22),
             ('x', 23),
             (';p', 24),
             (':%', 25)])[i]) for i in x.split())) for x in
"D F  E F  E C  E F  D C  J J  B B B  B A A  B A F  B B A  B A D  F I  \
D C  B B H  B B G  B A C  E F  F G  D C  E F  E C  E F  B A  B B G  B \
B E  B C B  F I  B A  D C  D C  D C  D C  B A C  B B E  B B B  B A J  \
D C  B B G  B A F  B A J  B A B  D C  B A F  B A J  B B C  B B B  B B \
E  B B G  D C  B B F  B A I  B A B  B A B  B B C  B A  D C  D C  D C  \
D C  B A F  B A J  B B C  B B B  B B E  B B G  D C  B B B  B B F  B A \
 D C  D C  D C  D C  B A F  B A J  B B C  B B B  B B E  B B G  D C  B \
B F  B B B  J J  B A H  B A B  B B G  B A  D C  D C  D C  D C  B A F  \
B A J  B B C  B B B  B B E  B B G  D C  B B E  J H  B B A  B A A  B B \
B  B A J  B A  D C  D C  D C  D C  B A F  B A J  B B C  B B B  B B E  \
B B G  D C  B B F  B C B  B B F  B A  B A B  B C A  J J  B A B  B B C \
 B B G  D C  H F  B A B  B C B  J I  B B B  J H  B B E  B A A  H D  B \
B A  B B G  B A B  B B E  B B E  B B H  B B C  B B G  F I  B A  D C  D\
 C  D C  D C  B B C  B B E  B A F  B B A  B B G  E A  D E  I G  B B B \
 J J  C D E  D C  B A B  B B F  J J  B B B  B A I  B A E  B A B  B B H\
  D C  B B F  J H  B A F  B B E  E E  D C  B B B  J I  B B E  B A F  B\
 A D  J H  B A A  B B B  D D  D E  E B  B A  D C  D C  D C  D C  B B F\
  B C B  B B F  E G  B A B  B C A  B A F  B B G  E A  E B  B A  B A  B\
 A  B B F  B B B  J J  B A H  D C  G B  D C  B B F  B B B  J J  B A H \
 B A B  B B G  E G  B B F  B B B  J J  B A H  B A B  B B G  E A  B B F\
  B B B  J J  B A H  B A B  B B G  E G  G F  H A  J F  H D  H I  G J  \
I E  E E  D C  B B F  B B B  J J  B A H  B A B  B B G  E G  I D  H J  \
G H  H F  J F  G I  H B  I C  G F  H H  E B  B A  J I  B C B  B B G  B\
 A B  B B F  D C  G B  D C  B B E  J H  B B A  B A A  B B B  B A J  E \
G  J F  B B H  B B E  J H  B B A  B A A  B B B  B A J  E A  E J  F C  \
F H  E I  E B  B A  B A  B B E  D C  G B  D C  D E  J C  E I  F B  F B\
  J B  E J  F J  F B  E J  B A J  D E  B A  J J  D C  G B  D C  D E  J\
 C  E I  F B  F B  J B  E J  F J  F B  F E  B A J  D E  B A  B C B  D \
C  G B  D C  D E  J C  E I  F B  F B  J B  E J  F J  F B  F B  B A J  \
D E  B A  B A  B B B  B B F  E G  B B F  B C B  B B F  B B G  B A B  B\
 A J  E A  D E  J J  B A I  B A B  J H  B B E  D E  E B  B A  B A  B B\
 C  B B E  B A F  B B A  B B G  E A  E B  B A  B B C  B B E  B A F  B \
B A  B B G  E A  B B E  E D  D E  D E  D E  B A  H I  I D  E F  G I  B\
 B B  I D  B A  D C  E C  D C  D C  B A  D C  D C  E C  D C  E C  D C \
 E C  B A  D C  D C  D C  E C  D C  D C  D C  D C  B A  D C  D C  D C \
 D C  D C  E C  D C  E C  D C  D C  B A  D C  D C  D C  E C  D C  E C \
 B A  D C  D C  D C  D C  D C  D C  D C  E C  D C  B A  E C  E C  D C \
 D C  D C  D C  D C  D C  D C  D C  D C  B A  D C  D C  D C  D C  D C \
 D C  D C  D C  D C  D C  D C  B A  D C  D C  E C  D C  D C  D C  D C \
 D C  D C  D C  B A  D C  D C  D C  D C  B B I  B A B  B B E  B B F  C\
 C H  B B B  F I  D C  I G  E J  E G  E I  D C  B A  D C  D C  B C B  \
B B B  B B H  B B G  B B H  J I  B A B  D C  J J  B A E  J H  B B A  B\
 B A  B A B  B A I  F I  D C  H I  B A B  J H  B B E  D C  I D  B A E \
 B A B  B A I  J I  B C B  D C  E D  D C  J J  B A E  F B  F B  J J  B\
 A E  J F  E I  B C A  E I  J H  B A  I A  B B B  B B J  B A B  B B E \
 B A B  B A A  D C  J I  B C B  F I  D C  B B A  B A B  J H  B B E  D \
C  B B F  B A E  B A B  B A I  J I  B C B  E H  J J  B A E  F B  F B  \
J J  B A E  E G  E I  B C A  E I  J H  E G  E G  E G  J C  B B A  J C \
 B B A  D E  D E  D E  E B  B A  B B G  B B E  B C B  F I  B A  D C  D\
 C  D C  D C  B A F  B B C  D C  G B  D C  B A F  B B A  B B C  B B H \
 B B G  E A  J J  E D  D E  H D  I A  D C  G C  G C  F I  D C  D E  E \
B  B A  D C  D C  D C  D C  B B C  B B B  B B E  B B G  D C  G B  D C \
 B A F  B B A  B B G  E A  B A F  B B A  B B C  B B H  B B G  E A  J J\
  E D  D E  I A  B B B  B B E  B B G  J H  D C  G C  G C  F I  D C  D \
E  E B  E B  B A  B A B  B C A  J J  B A B  B B C  B B G  D C  H F  B \
A B  B C B  J I  B B B  J H  B B E  B A A  H D  B B A  B B G  B A B  B\
 B E  B B E  B B H  B B C  B B G  F I  B A  D C  D C  D C  D C  B B C \
 B B E  B A F  B B A  B B G  E A  B B E  E D  D E  I G  B B B  J J  C \
D E  D C  B A B  B B F  J J  B B B  B A I  B A E  B A B  B B H  D C  B\
 B F  J H  B A F  B B E  E E  D C  B B B  J I  B B E  B A F  B A D  J \
H  B A A  B B B  D D  D E  E B  B A  D C  D C  D C  D C  B B F  B C B \
 B B F  E G  B A B  B C A  B A F  B B G  E A  E B  B A  D C  D C  D C \
 D C  B A  B B B  B B F  E G  B B F  B C B  B B F  B B G  B A B  B A J\
  E A  D E  J J  B A I  B A B  J H  B B E  D E  E B  B A  B B C  B B E\
  B A F  B B A  B B G  E A  B C B  E D  D E  J B  D C  D C  D C  D C  \
D C  D C  D C  D C  D C  D C  D C  D C  D C  D C  D C  D C  D C  D C  \
D C  D C  J D  D C  E I  D H  D E  E B  B A  B B F  B A I  B A B  B A \
B  B B C  E A  E J  E B  B A  B B B  B B F  E G  B B F  B C B  B B F  \
B B G  B A B  B A J  E A  D E  J J  B A I  B A B  J H  B B E  D E  E B\
  B A  B B C  B B E  B A F  B B A  B B G  E A  B C B  E D  D E  J B  G\
 B  G B  G B  G B  G B  D C  D C  D C  D C  D C  D C  D C  D C  D C  D\
 C  D C  D C  D C  D C  D C  J D  D C  F A  F D  D H  D E  E B  B A  B\
 B F  B A I  B A B  B A B  B B C  E A  E J  E B  B A  B B B  B B F  E \
G  B B F  B C B  B B F  B B G  B A B  B A J  E A  D E  J J  B A I  B A\
 B  J H  B B E  D E  E B  B A  B B C  B B E  B A F  B B A  B B G  E A \
 B C B  E D  D E  J B  G B  G B  G B  G B  G B  G B  G B  G B  G B  G \
B  D C  D C  D C  D C  D C  D C  D C  D C  D C  D C  J D  D C  F D  E \
I  D H  D E  E B  B A  B B F  B A I  B A B  B A B  B B C  E A  E J  E \
B  B A  B B B  B B F  E G  B B F  B C B  B B F  B B G  B A B  B A J  E\
 A  D E  J J  B A I  B A B  J H  B B E  D E  E B  B A  B B C  B B E  B\
 A F  B B A  B B G  E A  B C B  E D  D E  J B  G B  G B  G B  G B  G B\
  G B  G B  G B  G B  G B  G B  G B  G B  G B  G B  D C  D C  D C  D C\
  D C  J D  D C  F F  F D  D H  D E  E B  B A  B B F  B A I  B A B  B \
A B  B B C  E A  E J  E B  B A  B B B  B B F  E G  B B F  B C B  B B F\
  B B G  B A B  B A J  E A  D E  J J  B A I  B A B  J H  B B E  D E  E\
 B  B A  B B C  B B E  B A F  B B A  B B G  E A  B C B  E D  D E  J B \
 G B  G B  G B  G B  G B  G B  G B  G B  G B  G B  G B  G B  G B  G B \
 G B  G B  G B  G B  G B  G B  J D  D C  E J  E I  E I  D H  D E  E B \
 B A  B B F  B A I  B A B  B A B  B B C  E A  F B  E B  B A  B B B  B \
B F  E G  B B F  B C B  B B F  B B G  B A B  B A J  E A  D E  J J  B A\
 I  B A B  J H  B B E  D E  E B  B A  B B F  B A B  B B A  B B G  D C \
 G B  D C  E I  B A  B A  B A  B B J  B A E  B A F  B A I  B A B  D C \
 I E  B B E  B B H  B A B  F I  B A  D C  D C  D C  D C  B B F  B B B \
 J J  B A H  E G  B B F  B A B  B B A  B A A  B B G  B B B  E A  J I  \
B C B  B B G  B A B  B B F  E E  D C  E A  B A F  B B C  E E  B B C  B\
 B B  B B E  B B G  E B  E B  B A  D C  D C  D C  D C  B B F  B A B  B\
 B A  B B G  D C  G B  D C  B B F  B A B  B B A  B B G  D C  E D  D C \
 E J  B A  D C  D C  D C  D C  B B C  B B B  B B E  B B G  D C  G B  D\
 C  B B C  B B B  B B E  B B G  D C  E D  D C  E J  B A  D C  D C  D C\
  D C  B B C  B B E  B A F  B B A  B B G  D C  E A  B B E  E D  D E  J\
 B  I C C G  J D  D H  B B F  D C  G F  I E  G F  G H  G F  H I  G I  \
H J  D C  D H  B B F  D C  I A  G F  I C  G F  D C  G H  G F  H I  G H\
  G J  H G  G F  I C  D C  J E  G H  D C  D H  B B F  D C  G A  G A  G\
 A  G C  G C  G C  D E  D H  E A  B B F  B A B  B B A  B B G  E E  B A\
 F  B B C  E E  B B C  B B B  B B E  B B G  E B  E B  B A  D C  D C  D\
 C  D C  B A  D C  D C  D C  D C  B A  D C  D C  D C  D C  B A F  B A \
C  D C  B B C  B B B  B B E  B B G  D C  G B  G B  D C  F E  F D  F D \
 F B  F D  F I  B A  D C  D C  D C  D C  D C  D C  D C  D C  B B C  B \
B B  B B E  B B G  D C  G B  D C  E J  B A  D C  D C  D C  D C  D C  D\
 C  D C  D C  B A  B B G  B B E  B C B  F I  B A  D C  D C  D C  D C  \
B B C  B B E  B A F  B B A  B B G  D C  E A  B B E  E D  D E  J B  I C\
 C G  J D  D H  B B F  D C  G F  I E  G F  G H  G F  H I  G I  H J  D \
C  D H  B B F  D C  I A  G F  I C  G F  D C  G H  G F  H I  G H  G J  \
H G  G F  I C  D C  J E  G H  D C  D H  B B F  D C  G A  G A  G A  G C\
  G C  G C  D E  D H  E A  B B F  B A B  B B A  B B G  E E  B A F  B B\
 C  E E  B B C  B B B  B B E  B B G  E B  E B  B A  B A B  B C A  J J \
 B A B  B B C  B B G  D C  H F  B A B  B C B  J I  B B B  J H  B B E  \
B A A  H D  B B A  B B G  B A B  B B E  B B E  B B H  B B C  B B G  F \
I  B A  D C  D C  D C  D C  B B C  B B E  B A F  B B A  B B G  E A  B \
B E  E D  D E  I G  B B B  J J  C D E  D C  B A B  B B F  J J  B B B  \
B A I  B A E  B A B  B B H  D C  B B F  J H  B A F  B B E  E E  D C  B\
 B B  J I  B B E  B A F  B A D  J H  B A A  B B B  D D  D E  E B  B A \
 D C  D C  D C  D C  B B F  B C B  B B F  E G  B A B  B C A  B A F  B \
B G  E A  E B  B A  D C  D C  D C  D C  B A  B A"
.split("  ")])))
