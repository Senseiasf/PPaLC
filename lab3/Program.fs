open System

let calculateTuple (a, b) =
    (a + b, a * b)

let calculateCurried a b =
    (a + b, a * b)

let rec sumRange first last =
    if first > last then 0
    else first + sumRange (first + 1) last

let sumRangeTail first last =
    let rec loop current result =
        if current > last then result
        else loop (current + 1) (result + current)

    loop first 0

let rec red steps =
    if steps <= 0 then "Красный"
    else green (steps - 1)

and green steps =
    if steps <= 0 then "Зелёный"
    else yellow (steps - 1)

and yellow steps =
    if steps <= 0 then "Жёлтый"
    else red (steps - 1)

let sumTuple ((a, b, c), sum) =
    sum a b c

let sumCurried a b c sum =
    sum a b c

[<EntryPoint>]
let main _ =
    printfn "1. Функции, возвращающие кортеж"
    printfn "Кортежные параметры: %A" (calculateTuple (3, 4))
    printfn "Каррированные параметры: %A" (calculateCurried 3 4)

    printfn "\n2. Обычная рекурсия"
    printfn "Сумма чисел от 1 до 5: %d" (sumRange 1 5)

    printfn "\n3. Хвостовая рекурсия"
    printfn "Сумма чисел от 1 до 5: %d" (sumRangeTail 1 5)

    printfn "\n4. Конечный автомат: красный -> зелёный -> жёлтый"
    printfn "Начальное состояние: %s" (red 0)
    printfn "После 1 перехода: %s" (red 1)
    printfn "После 2 переходов: %s" (red 2)
    printfn "После 3 переходов: %s" (red 3)

    printfn "\n5. Три числа и лямбда-выражение"
    printfn "Кортежная форма: %d" (sumTuple ((1, 2, 3), fun a b c -> a + b + c))
    printfn "Каррированная форма: %d" (sumCurried 1 2 3 (fun a b c -> a + b + c))

    Console.ReadLine() |> ignore
    0

