import columnize

a = """APPELflapsss0604
ArcaneHeirophant
ArcaneMagicGirl
BigFatMamaLlamaa
CapixKW
ChipDuBot
ChipDuPug
CrazeeGamar27
CupOCopper
DeathAdder18
EnderAki
EpsilonEngineer
FlashMigma
GhoulMF
GrandmasterGrant
Hazzaaaaa
IcyGenius
J0kaKinG
J_gov
Jadyks
Khan_Stark
KlausGaming
Latissimuss
LivvyK
LoycSTV
MC_Wza
MNe_Pyro
Matei
Mekhami
MetallicAlter
MrBlackBlade
Nanor9
NapalmMayhem
ObvsNotElvis
Overk1ll_Phil
PitconiX
RettiSeti
Rhyken_
Runa88
Stormloop
Teh_Bears
Thedragonball
UpsettiResetti
Viktor40
Void64
_LoonLoon_
albertopv098
buggy9000
couchlion
dafynw
e1by
frostiebits
iGhostx0123
itakashiraiya
jjfeldcher
jorisenhendrik
killermanjer
lioncouch
minecone12
sony3000
vktec"""

a = a.split('\n')

print(columnize.columnize(a, displaywidth=55, colsep=' | '))
