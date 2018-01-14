from Cheetah.Template import Template
from subprocess import call

# Python Cheetah template for French Phrase Flashcards

templateDef = """
\\documentclass[xcolor=dvipsnames]{beamer}
\\usepackage{listings}
\\usepackage{color}
\\usepackage{graphicx}
\\mode<presentation> {
  \\usetheme{Madrid}
  \\setbeamercolor{frametitle}{fg=BurntOrange}
  \\setbeamercolor*{palette primary}{use=structure,fg=Sepia}
  \\setbeamercolor*{palette secondary}{use=structure,fg=Sepia}
  \\setbeamercolor*{palette tertiary}{use=structure,fg=Sepia}
  \\setbeamerfont{frametitle}{size=\\huge}
}

\\pagenumbering{none}
\\setbeamertemplate{footline}{}
\\setbeamercovered{transparent}

\\begin{document}

\\begin{frame}
  \\begin{quotation}
   {\\fontsize{\\textheight}{\\textheight}\\selectfont $title }
  \\end{quotation}
\\end{frame}

\\begin{frame}
\\begin{center}
  {Intentionally Left Blank}
\\end{center}
\\end{frame}

#for $word in $dict
\\begin{frame}
\\begin{center}
  {\\fontsize{.5\\textheight}{.5\\textheight}\\selectfont  $word['english']}
#if 'note' in $word
\\\\($word['note'])
#end if
\\end{center}
\\end{frame}

\\begin{frame}
\\begin{center}
  {\\fontsize{.25\\textheight}{.25\\textheight}\selectfont 
\\vbox{{\\Huge $word['english']:} \\\\ $word['french']}}
\end{center}
\end{frame}

#end for

\\end{document}
"""

namespace={'title': 'Useful French Phrases',
    'dict': [
    {'english': 'Thank you', 'french': 'Merci'},
    {'english': 'Thank you very much', 'french': 'Merci beaucoup'},
    {'english': 'Good day', 'french': 'Bonjour'},
    {'english': 'Good evening', 'french': 'Bonsoir'},
    {'english': 'Good night', 'french': 'Bonne nuit', 'note': 'going to bed'},
    {'english': 'Please', 'french': "S\\'il vous pla\\^it"},
    {'english': 'Goodbye', 'french': 'Au revoir'},
    {'english': "You're welcome", 'french': 'De rien'},
    {'english': "See you tomorrow", 'french': 'A demain'},
    {'english': "Yes", 'french': 'Oui'},
    {'english': "No", 'french': 'Non'},
    {'english': "I'm sorry", 'french': "Je suis d\\'esol\\'e"},
    {'english': "Excuse me", 'french': "Pardon"},
    {'english': "Let's go", 'french': "Allons-y"},
    {'english': "How are you?", 'french': "Comment allez-vous ?", 'note': 'formal'},
    {'english': "How are you?", 'french': "\\c{c}a va ?", 'note': 'informal'},
    {'english': "Very good", 'french': "Tre\\'s bien"},
    {'english': "I'm fine", 'french': "Je vais bien"},
    {'english': "I'm fine", 'french': "\\c{c}a va", 'note': 'In response to \\c{c}a va'},
    {'english': "bad", 'french': "mal"},
    {'english': "My name is", 'french': "je m'appelle"},
    {'english': "Nice to meet you", 'french': "Enchant\\'e"},
    {'english': "Mister", 'french': "Monsieur"},
    {'english': "Mrs.", 'french': "Madame"},
    {'english': "Miss", 'french': "Mademoiselle"},
    {'english': "Where are you from?", 'french': "Vous \\^etes d'o\\'u ?", 'note': 'formal'},
    {'english': "Where are you from?", 'french': "Tu es d'o\\'u ?", 'note': 'informal'},
    {'english': "I am from", 'french': "Je suis de"},
    {'english': "How old are you?", 'french': "Quel \\^age avez-vous ?", 'note': 'formal'},
    {'english': "How old are you?", 'french': "Tu as quel \\^age ?", 'note': 'informal'},
    {'english': "I am \\rule{1cm}{2pt} years old", 'french': "J'ai \\rule{1cm}{2pt} ans"},
    {'english': "Do you speak French?", 'french': "Parlez-vous fran\\c{c}ais ?", 'note': 'formal'},
    {'english': "Do you speak French?", 'french': "Tu parles anglais ?", 'note': 'informal'},
    {'english': "French", 'french': "l'fran\\c{c}ais"},
    {'english': "English", 'french': "l'anglais"},
    {'english': "Spanish", 'french': "l'espagnol"},
    {'english': "Do you understand?", 'french': "Tu comprends"},
    {'english': "Do you understand?", 'french': "Es que vous comprenez ?"},
    {'english': "I understand", 'french': "Je comprends"},
    {'english': "I don't understand", 'french': "Je ne comprends pas"},
    {'english': "I don't know", 'french': "Je ne sais pas"},
    {'english': "Of course", 'french': "Bien s\^ur"},
    {'english': "Where is", 'french': "O\'u est"},
    {'english': "Where are", 'french': "O\'u sont"},
    {'english': "Here is", 'french': "Voici"},
    {'english': "There it is", 'french': "Voil\\'a"},
    {'english': "There is/are", 'french': "Il y a"},
    {'english': "There was", 'french': "Il y avait"},
    {'english': "I'm vegetarian", 'french': "Je suis v\\'eg\\'etarien"},
    {'english': "How do you say \\rule{1cm}{2pt} in French?", 'french': "Comment dit-on \\rule{1cm}{2pt} en fran\\c{c}ais ?"},
    {'english': "What is that?", 'french': "Qu'est-ce que c'est que \\c{c}a ?"},
    {'english': "What's the matter?", 'french': "Qu'est-ce qu'il y a ?"},
    {'english': "It doesn't matter", 'french': "\\c{C}a ne fait rien"},
    {'english': "What's happening?", 'french': "Qu'est-ce qui se passe ?"},
    {'english': "I have no idea", 'french': "Je n'ai aucune id\'ee"},
    {'english': "I'm tired", 'french': "Je suis fatigu\'e"},
    {'english': "I'm sick", 'french': "Je suis malade"},
    {'english': "I'm hungry", 'french': "J'ai faim"},
    {'english': "I'm thirsty", 'french': "J'ai soif"},
    {'english': "I'm hot", 'french': "J'ai chaud"},
    {'english': "I'm cold", 'french': "J'ai froid"},
    {'english': "I'm bored", 'french': "Je m'ennuie"},
    {'english': "It's all the same to me.", 'french': "\\c{C}a m'est \\'egal"},
    {'english': "I don't care", 'french': "Je m'en fiche", 'note': 'informal'},
    {'english': "Don't worry!", 'french': "Ne vous en faites pas", 'note': 'formal'},
    {'english': "Don't worry!", 'french': "Ne t'en fais pas", 'note': 'informal'},
    {'english': "It's alright", 'french': "Ce n'est pas grave"},
    {'english': "I forgot", 'french': "J'ai oubli\'e"},
    {'english': "I have to go", 'french': "Je dois y aller"},
    {'english': "Bless you!", 'french': "A vos souhaits !", 'note': 'formal, sneeze'},
    {'english': "Bless you!", 'french': "A tes souhaits !", 'note': 'informal, sneeze'},
    {'english': "Congratulations!", 'french': "F\\'elicitations !"},
    {'english': "Good luck!", 'french': "Bonne chance !"},
    {'english': "It's your turn!", 'french': "C'est \\'a vous !", 'note': 'formal'},
    {'english': "It's your turn!", 'french': "C'est \\'a toi !", 'note': 'informal'},
    {'english': "Be quiet!", 'french': "Taisez-vous !", 'note': 'formal'},
    {'english': "Be quiet!", 'french': "Tais-toi !", 'note': 'informal'},
    {'english': "I love you", 'french': "Je vous aime", 'note': 'formal/plural'},
    {'english': "I love you", 'french': "Je t'aime", 'note': 'informal'},
    {'english': "Here", 'french': "Tenez", 'note': 'formal; handing something'},
    {'english': "Here", 'french': "Tiens", 'note': 'informal; handing something'},
    {'english': "What's new?", 'french': "Quoi de neuf ?"},
    {'english': "Not much", 'french': "Pas grand-chose"},
    {'english': "my pet", 'french': "mon animal"},
    {'english': "I have a pet", 'french': "J'ai un animal"},
    {'english': "a dog", 'french': "un chien"},
    {'english': "a cat", 'french': "un chat"},
    {'english': "a tortoise", 'french': "une tortue"},
    {'english': "a rabbit", 'french': "un lapin"},
    {'english': "a bird", 'french': "un oiseau"},
    {'english': "a fish", 'french': "un poisson"},
    {'english': "a hamster", 'french': "un hamster"},
    {'english': "a mouse", 'french': "un souris"},
    {'english': "a horse", 'french': "un cheval"},                                
]}

phrases = 'phrases.tex'
open(phrases, 'w').write(str(Template(templateDef, searchList=[namespace])))
call(["pdflatex", phrases])

namespace = {'title': 'Useful French Words',
    'dict': [
        {'english': 'Blue', 'french': 'bleu (e)'},
        {'english': 'green', 'french': 'vert (e)'},
        {'english': 'purple', 'french': 'violet (e)'},
        {'english': 'grey', 'french': 'gris (e)'},
        {'english': 'white', 'french': 'blanc (e)'},
        {'english': 'red', 'french': 'rouge'},
        {'english': 'orange', 'french': 'orange'},
        {'english': 'pink', 'french': 'rose'},
        {'english': 'brown', 'french': 'marron'},
        {'english': 'yellow', 'french': 'jaune'},
        {'english': 'zero', 'french': "z\\'ero"},
        {'english': 'one', 'french': "un"},
        {'english': 'two', 'french': "deux"},
        {'english': 'three', 'french': "trois"},
        {'english': 'four', 'french': 'quatre'},
        {'english': 'five', 'french': 'cinq'},
        {'english': 'six', 'french': 'six'},
        {'english': 'seven', 'french': 'sept'},
        {'english': 'eight', 'french': 'huit'},
        {'english': 'nine', 'french': 'neuf'},
        {'english': 'ten', 'french': 'dix'},
        {'english': 'eleven', 'french': 'onze'},
        {'english': 'twelve', 'french': 'douze'},
        {'english': 'thirteen', 'french': 'treize'},
        {'english': 'fourteen', 'french': 'quatorze'},
        {'english': 'fifteen', 'french': 'quinze'},
        {'english': 'sixteen', 'french': 'seize'},
        {'english': 'seventeen', 'french': 'dix-sept'},
        {'english': 'eighteen', 'french': 'dix-huit'},
        {'english': 'nineteen', 'french': 'dix-neuf'},
        {'english': 'twenty', 'french': 'vingt'},
        {'english': 'thirty', 'french': 'trente'},
        {'english': 'fourty', 'french': 'quarante'},
        {'english': 'fifty', 'french': 'cinquante'},
        {'english': 'sixty', 'french': 'soixante'},
        {'english': 'seventy', 'french': 'soixante-dix'},
        {'english': 'eighty', 'french': 'quatre-vingts'},
        {'english': 'ninety', 'french': 'quatre-vingt-dix'},
        {'english': 'one hundred', 'french': 'cent'},
    ]
}
     
words = 'words.tex'
open(words, 'w').write(str(Template(templateDef, searchList=[namespace])))
call(["pdflatex", words])
