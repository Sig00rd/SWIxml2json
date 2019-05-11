Używałem pythona w wersji 3.7.

Przyjąłem następujące konwencje w sytuacjach co do których miałem wątpliwości:
    1) plik wejściowy umieszczany jest w katalogu SWI, plik wyjściowy jest zapisywany w tym katalogu

    2) w przypadku, gdy istnieje już plik output.json, zostanie on nadpisany

    3) skrypt python do uruchomienia znajduje się w folderze source, dla przejrzystości dodatkowe pliki umieściłem
        w katalogu source/utils

    4) odnośnie ignorowania "obiektów, które posiadają niewspierane słowa kluczowe" - na początku zrozumiałem to jako
        ignorowanie całych obiektów jeżeli mają niewspierane pola, ale case kolorowych kredek B w treści zadania
        pokazuje ignorowanie tylko pola - przyjąłem konwencję zgodną z plikiem wynikowym z treści zadania, gdyby
        jednak chodziło o ignorowanie całego obiektu, wystarczy ustawić flagę SKIP_OBJECTS_WITH_UNSUPPORTED_KEYWORDS
        w source/utils/config.py na True

    5) odnośnie niepoprawnych obiektów - ignorowane są obiekty niepoprawne wg. logiki zadania ale także te, w których
        xml jest nieprawidłowy (np. niedomknięty znacznik w którymś polu) i ElementTree zgłosi błąd parsowania

    6) odnośnie niedrukowalnych znaków - przyjąłem konwencję ignorowania całego obiektu jeżeli gdziekolwiek w jego xml
        wystąpił niedrukowalny znak