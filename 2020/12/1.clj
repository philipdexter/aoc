
(load-file "../common/common.clj")

(defn parse [line]
  [(subs line 0 1) (to-int (subs line 1))])

(def directions (vec (map parse input)))

(defn handle [[facing x y] [dir amt]]
  (case dir
    "N" [facing x (+ y amt)]
    "S" [facing x (- y amt)]
    "E" [facing (+ x amt) y]
    "W" [facing (- x amt) y]
    "F" [facing
         (case facing
           0 (+ x amt)
           180 (- x amt)
           x)
         (case facing
           90 (+ y amt)
           270 (- y amt)
           y)]
    "L" [(mod (+ facing amt) 360) x y]
    "R" [(mod (- facing amt) 360) x y]))

(let
  [[_ x y] (reduce handle [0 0 0] directions)]
  (+ (abs x) (abs y)))
