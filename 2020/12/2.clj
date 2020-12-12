
(load-file "../common/common.clj")

(defn parse [line]
  [(subs line 0 1) (to-int (subs line 1))])

(def directions (vec (map parse input)))

(defn handle [[x y w-x w-y] [dir amt]]
  (case dir
    "N" [x y w-x (+ w-y amt)]
    "S" [x y w-x (- w-y amt)]
    "E" [x y (+ w-x amt) w-y]
    "W" [x y (- w-x amt) w-y]
    "F" [(+ x (* amt w-x)) (+ y (* amt w-y)) w-x w-y]
    "L" [x y
         (case amt
           90 (- w-y)
           180 (- w-x)
           270 w-y
           360 w-x)
         (case amt
           90 w-x
           180 (- w-y)
           270 (- w-x)
           360 w-y)]
    "R" [x y
         (case amt
           90 w-y
           180 (- w-x)
           270 (- w-y)
           360 w-x)
         (case amt
           90 (- w-x)
           180 (- w-y)
           270 w-x
           360 w-y)]))

(let
  [[x y w-x w-y] (reduce handle [0 0 10 1] directions)]
  (+ (abs x) (abs y)))
