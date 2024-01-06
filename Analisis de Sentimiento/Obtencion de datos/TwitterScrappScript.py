import time

# args
import argparse

from ntscraper import Nitter
import pandas as pd

# Words to use in classes by tweeter


def main(args):

    # JOYFUL
    daring_words = ['audaz', 'valiente', 'osado', 'atrevido', 'intrépido',  'indomable', 'imparable', 'tenaz', 'osadía', 'despreocupado', 'indiferente', 'imperturbable','desvergonzado', 'sin miedo']

    optimistic_words = ['optimista', 'positivo', 'esperanzador', 'brillante', 'alegre', 'entusiasta', 'confiado', 'animado', 'motivado', 'esperanzado', 'constructivo', 'radiante', 'inspirador', 'proactivo', 'bueno', 'afortunado', 'alentador', 'sonriente', 'vibrante', 'optimismo', 'gratitud', 'triunfante', 'exitoso', 'esperanza', 'felicidad', 'alegría', 'luminoso', 'prometedor', 'valiente', 'decidido', 'determinado', 'resiliente', 'triunfo', 'buena onda', 'buena vibra', 'satisfecho', 'apasionado', 'aliento']

    playful_words = ['juguetón', 'divertido', 'travieso', 'alegre', 'animado', 'bromista', 'risueño', 'festivo', 'gracioso', 'juerguista', 'chispeante', 'espontáneo', 'travieso', 'jovial', 'travesura', 'festividad', 'entretenido', 'lúdico', 'chistoso', 'vivaz', 'pícaro', 'jocoso', 'colorido', 'jugoso', 'retozón', 'ligero', 'despreocupado', 'creativo', 'curioso', 'risueño', 'jugoso', 'cómico', 'alegría', 'festivo', 'festín', 'animado', 'travesura', 'inquieto', 'expresivo', 'brincón']


    # POWERFUL
    surprised_words = ['sorprendido', 'asombrado', 'estupefacto', 'atónito', 'maravillado', 'desconcertado', 'boquiabierto', 'perplejo', 'incrédulo', 'asombroso', 'incredulidad', 'extrañado', 'atónito', 'impactado', 'anonadado', 'deslumbrado', 'atónito', 'desconcertado', 'desorientado', 'estupefacto', 'boquiabierto', 'asombroso', 'deslumbrante', 'estupefacto', 'atónito', 'estupefacción', 'conmocionado', 'desconcertado', 'aturdido', 'asombro', 'sobresaltado', 'maravilloso', 'atónito', 'desconcertante', 'impresionante', 'incredulidad', 'asombrado', 'impactante', 'estupefacto']

    successful_words = ['exitoso', 'triunfante', 'logrado', 'prosperidad', 'realizado', 'triunfo', 'victorioso', 'efectivo', 'triunfador', 'cumplido', 'satisfactorio', 'productivo', 'próspero', 'conquista', 'logro', 'brillante', 'triunfal', 'excelente', 'cumplimiento', 'triunfo', 'triunfante', 'ganador', 'conquista', 'éxito', 'provechoso', 'provechoso', 'triunfal', 'triunfador', 'conseguido', 'admirable', 'alcanzado', 'sobresaliente', 'glorioso', 'inspirador', 'realización', 'triunfo', 'realizador', 'exitosamente', 'recompensado']

    confident_words = ['confiado', 'seguro', 'convencido', 'decidido', 'resuelto', 'determinado', 'autoconfianza', 'seguridad', 'firmeza', 'valiente', 'audaz', 'positivo', 'optimista', 'capaz', 'competente', 'sosegado', 'sereno', 'tranquilo', 'assertivo', 'optimismo', 'autoestima', 'decidido', 'intrépido', 'resoluto', 'inquebrantable', 'imparable', 'fuerte', 'poderoso', 'invencible', 'vigoroso', 'tenaz', 'firme', 'inamovible', 'robusto', 'autovaloración', 'sin dudar', 'inamovible', 'indomable', 'sin vacilaciones']


    # PEACEFUL
    secure_words = ['seguro', 'protegido', 'resguardado', 'tranquilo', 'confiado', 'apacible', 'sin preocupaciones', 'resuelto', 'protección', 'calmado', 'asegurado', 'estable', 'fiable', 'blindado', 'inquebrantable', 'sereno', 'firme', 'confianza', 'certeza', 'solidez', 'tranquilidad', 'estabilidad', 'garantizado', 'incólume', 'confiable', 'escudo', 'confiabilidad', 'resistente', 'inamovible', 'protegido', 'incólume', 'incuestionable', 'inmutable', 'sosegado', 'intocado', 'salvaguarda', 'inquebrantable', 'consistente']

    thankful_words = ['agradecido', 'grato', 'reconocido', 'apreciativo', 'gratitud', 'reconocimiento', 'gracias', 'bendecido', 'agradecimiento', 'agradecido', 'gratificante', 'reconocido', 'gratitud', 'reconocimiento', 'aprecio', 'dank', 'obligado', 'reconocido', 'apreciado', 'bendición', 'dar gracias', 'dar las gracias', 'agradecimiento', 'valorado', 'agradecimiento', 'reverente', 'reconocido', 'gracias', 'dar las gracias', 'satisfecho', 'humbled', 'honorado', 'contento', 'gracias', 'dar las gracias', 'reverencia', 'humilde', 'beneficiado']


    loving_words = ['amoroso', 'te amo', 'amor', 'tierno', 'apasionado', 'compasivo', 'dulce', 'devoto', 'bondadoso', 'comprensivo', 'atento', 'gentil', 'afable', 'ternura', 'caloroso', 'sincero', 'cordial', 'amistoso', 'afecto', 'entrañable', 'adorable', 'compañero', 'solidario', 'intenso', 'amistad', 'afectividad', 'dulzura', 'sensibilidad', 'compañerismo', 'comprometido', 'cálido', 'emotivo', 'conmovedor', 'ferviente', 'apoyo', 'leal', 'familiar', 'cuidadoso', 'generoso']

    relaxed_words = ['relajado', 'tranquilo', 'calmado', 'sereno', 'apacible', 'descansado', 'sosegado', 'sin tensiones', 'despreocupado', 'plácido', 'pausado', 'distendido', 'desestresado', 'suave', 'pacifico', 'suelto', 'libre', 'sosegado', 'reposado', 'desconectado', 'tranquilizado', 'descansado', 'deliciosamente tranquilo', 'desahogado', 'sin presiones', 'holgado', 'relajación', 'comodidad', 'descanso', 'liberado', 'sin preocupaciones', 'regocijado', 'fresco', 'holgazán', 'libre de estrés', 'sin apuros', 'sin presión', 'en paz']

    responsive_words = ['responsivo', 'sensible', 'atento', 'reactivo', 'rápido para adaptarse', 'ágil', 'rápido', 'flexible', 'pronto para responder', 'rápido para actuar', 'alerta', 'rápido para entender', 'rápido para reaccionar', 'pronto para ayudar', 'rápido para resolver', 'rápido para cambiar', 'rápido para aprender', 'rápido para colaborar', 'rápido para ajustarse', 'rápido para entender', 'rápido para implementar', 'pronto para participar', 'rápido para comunicar', 'pronto para comprometerse', 'rápido para colaborar', 'rápido para apoyar', 'rápido para integrarse', 'rápido para adaptarse', 'rápido para asumir responsabilidades', 'rápido para abordar problemas', 'rápido para solucionar problemas', 'rápido para innovar']

    # SAD
    sleepy_words = ['somnoliento', 'adormilado', 'cansado', 'fatigado', 'flojera', 'apacible', 'soñoliento', 'amodorrado', 'adormecido', 'dormilón', 'agotado', 'cansado', 'abatido', 'sosegado', 'soñador', 'abrumado', 'letargo', 'adormecido', 'rendido', 'sonoliento', 'sosegado', 'cansancio', 'modorro', 'cabezada', 'débil', 'estancado', 'pesadez', 'agotamiento', 'adormilamiento', 'ensueño', 'lenitivo', 'dormido', 'abatimiento', 'sedante', 'amodorramiento', 'entumecido', 'embotado', 'sedación']

    isolated_words = ['aislado', 'solitario', 'desconectado', 'marginado', 'soltero', 'abandonado', 'solitario', 'excluido', 'incomunicado', 'separado', 'solitario', 'desamparado', 'apartado', 'rechazado', 'solitario', 'desatendido', 'solitario', 'solitario', 'exiliado', 'solitario', 'solitario', 'solitario', 'solitario', 'solitario', 'desolado', 'solitario', 'solitario', 'solitario', 'solitario', 'solitario', 'solitario', 'solitario', 'solitario', 'solitario', 'solitario', 'solitario', 'solitario', 'solitario', 'solitario', 'solitario', 'solitario']


    stupid_words = ['estupido', 'pendejo','desorientado', 'desconcertado', 'perplejo', 'despistado', 'perdido', 'embrollado', 'incomprensible', 'atolondrado', 'desconcertante', 'desorientador', 'enredado', 'obscuro', 'desordenado', 'desorganizado', 'complicado']


    # MAD
    distant_words = ['distante', 'lejano', 'alejado', 'remoto', 'distanciado', 'desconectado', 'apartado', 'retirado', 'inaccesible', 'solitario', 'aislado', 'separado', 'reservado', 'frio', 'indiferente', 'pasivo', 'distraído', 'ausente', 'desapegado', 'inaccesible', 'desvinculado', 'reservado', 'alejamiento', 'incomunicado', 'apartado', 'indiferencia', 'falta de cercanía', 'desinteresado', 'alejamiento', 'sollozante', 'receloso', 'esquivo', 'desconectado', 'lejanía', 'desatento', 'desvinculado', 'apartado', 'poco afectivo', 'evitativo']

    frustrated_words = ['frustrado',  'desalentado', 'abrumado', 'molesto', 'exasperado', 'insatisfecho', 'desilusionado', 'agitado', 'incomprendido', 'furioso', 'irritante', 'impotente', 'contrariado', 'harto', 'enfadado', 'amargado', 'desesperado', 'cansado', 'irritable', 'nervioso', 'abatido', 'triste', 'descontento', 'rabioso', 'agobiado', 'enfurecido', 'desmoralizado', 'enervado', 'dolido', 'resentido', 'enfadado', 'exacerbado', 'consternado', 'desconcertado', 'preocupado', 'incómodo', 'perplejo', 'desilusionado']

    irritated_words = ['irritado', 'molesto', 'exasperado', 'enfadado', 'inquieto', 'furioso', 'irascible', 'fastidiado', 'nervioso', 'impaciente', 'indignado', 'enojado', 'exasperante', 'irritable', 'contrariado', 'enojoso', 'desagradable', 'hostil', 'iracundo', 'incómodo', 'amargado', 'enervante', 'irritante', 'furibundo', 'iracundo', 'harto', 'ofuscado', 'aborrecido', 'exacerbado', 'alterado', 'agresivo', 'iracundo', 'violento', 'irascible', 'agobiado', 'intranquilo', 'enfurecido', 'descontento', 'furioso', 'amargado', 'resentido']

    jealous_words = ['celoso', 'envidioso', 'resentido', 'despechado', 'inseguro', 'poseído', 'verde de envidia', 'compulsivo', 'competitivo', 'dolorido', 'rabioso', 'amargado', 'molesto', 'frustrado', 'afectado', 'malhumorado', 'tenso', 'hostil', 'incomprendido', 'angustiado', 'insatisfecho', 'obsesionado', 'vigilante', 'preocupado', 'dolido', 'amargura', 'rencoroso', 'insatisfecho', 'resentido', 'desconfiado', 'insatisfecho', 'preocupado', 'dolido', 'vigilante', 'inseguro', 'incomprendido', 'competitivo', 'obsesivo', 'descontento', 'afectado']


    # SCARED
    embarrassed_words = ['avergonzado', 'incomodo', 'mortificado', 'sonrojado', 'timido', 'confundido', 'culpable', 'desconcertado', 'titubeante', 'apenado', 'torpe', 'desconcertado', 'incómodo', 'autoconsciente', 'abrumado', 'nervioso', 'aprensivo', 'tímido', 'apenado', 'desorientado', 'humillado', 'inquieto', 'mortificado', 'ruborizado', 'cohibido', 'azorado', 'atolondrado', 'contrariado', 'incómodo', 'chismoso', 'irritado', 'indignado', 'perturbado', 'inhibido', 'torpe', 'tartamudo', 'rígido', 'confuso', 'desprevenido', 'ruborizado']

    overwhelmed_words = ['abrumado', 'desbordado', 'sobrecargado', 'desbordante', 'agitado', 'inundado', 'colapsado', 'desbordado', 'preocupado', 'perdido', 'incapacitado', 'saturado', 'atrapado', 'agobiado', 'abatido', 'estresado', 'sobrepasado', 'atolondrado', 'confundido', 'angustiado', 'agotado', 'desordenado', 'desesperado', 'consumido', 'perdido', 'aturdido', 'aplastado', 'desorientado', 'subyugado', 'perplejo', 'sofocado', 'atónito', 'rendido', 'abatido', 'sin aliento', 'desconcertado', 'aniquilado', 'sin escapatoria', 'incontrolable']

    # 
    sentiments = {
        'joyful': {
            'daring': daring_words,
            'optimistic': optimistic_words,
            'playful': playful_words
        },
        'powerful': {
            'surprised': surprised_words,
            'successful': successful_words,
            'confident': confident_words
        },
        'peaceful': {
            'secure': secure_words,
            'thankful': thankful_words,
            'loving': loving_words,
            'relaxed': relaxed_words,
            'responsive': responsive_words
        },
        'sad': {
            'sleepy': sleepy_words,
            'isolated': isolated_words,
            'stupid': stupid_words,
            
        },
        'mad': {
            'distant': distant_words,
            'frustrated': frustrated_words,
            'irritated': irritated_words,
            'jealous': jealous_words
        },
        'scared': {
            'embarrassed': embarrassed_words,
            'overwhelmed': overwhelmed_words
        }
    }

    # Getting Tweets ;)


    scraper = Nitter(0)

    number_of_tweets = 3
    columns = ['user', 'text', 'date', 'emotion', 'sentiment']


    sentiment_dataframe = pd.DataFrame(columns=columns)

    for sentiment in sentiments:
        for emotion in sentiments[sentiment]:
            
            terms= sentiments[sentiment][emotion][0:3]
            print(terms)

            tweets = scraper.get_tweets(terms, mode = 'term',number = number_of_tweets)
            print(emotion, tweets)
            recopilation = []
            for tweet in tweets[0]['tweets']:
                data = [tweet['user']['username'], tweet['text'],tweet['date'], emotion, sentiment]
                recopilation.append(data)
            
            
            dataframe = pd.DataFrame(recopilation, columns=columns)
            dataframe.to_csv(f'./DataFrames/{sentiment}_{emotion}.csv', index=False)

            sentiment_dataframe = sentiment_dataframe.append(dataframe, ignore_index=True)


    sentiment_dataframe.to_csv('./sentiment_dataframe.csv', index=False)

        


# run script
if __name__ == "__main__":
    # add space in logs
    print("\n\n")
    print("*" * 60)
    start = time.time()

    # parse args
    args = parse_args()

    # run main function
    main(args)

    end = time.time()
    print("\n\n")
    print("Total time taken: {}s (Wall time)".format(end - start))
    # print("max number of K length: {}".format(args.k_length))
    # add space in logs
    print("*" * 60)
    print("\n\n")