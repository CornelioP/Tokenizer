from tokenizer import BPE


if __name__ == '__main__':
    
    training_test = "Le sue idee si concretizzarono con la fondazione delle Olimpiadi moderne nel corso del Congresso Olimpico del 1894, in cui fu affidata ad Atene l'organizzazione dei Giochi della I Olimpiade del 1896 e venne formato il Comitato Olimpico Internazionale. Durante la presidenza di quest'organizzazione, terminata nel 1925, de Coubertin istituì alcuni simboli che sarebbero diventati fondamentali nel contesto sportivo, tra cui il motto olimpico Citius, Altius, Fortius, la bandiera a cinque cerchi e il giuramento; fu inoltre promotore della nascita dei Giochi olimpici invernali, con la prima edizione che si tenne a Chamonix nel 1924. In ambito educativo, il barone parigino costituì l'Éclaireurs Français, la prima organizzazione scout francese.De Coubertin ebbe una prolifica carriera letteraria, spaziando da trattati sportivi a opere educative, da testi storico-politici ad autobiografie; tra i 34 libri pubblicati figurano L'Evolution Française sous la Troisième République (1896), Histoire universelle (1920), Leçons de Pédagogie sportive (1921) e Mémoires olympiques (1932). Conquistò anche una medaglia d'oro per la letteratura alle Olimpiadi del 1912 con la poesia Ode allo Sport. Nel 1936 il CIO lo propose per il premio Nobel per la pace, «per i suoi sforzi nella riduzione delle tensioni mondiali attraverso la rinascita e l'organizzazione dei Giochi olimpici internazionali». Dopo la sua morte gli furono dedicati vari monumenti e onorificenze sportive, tra cui la medaglia Pierre de Coubertin."
    bpe = BPE(1000)
    
    bpe.train(training_test)
    
    decode = bpe.encode('Dio mio santo il signore sta roba funziona davvero')
    
    print('The decoded tokens are :', decode)
    
    encode = bpe.decode(decode)
    
    print('The encoded tokens are :', encode)