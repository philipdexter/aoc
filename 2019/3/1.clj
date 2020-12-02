
(load-file "../common/common.clj")

(def lines (file-lines "1.txt"))
; (def lines ["R8,U5,L5,D3" "U7,R6,D4,L4"])
; (def lines ["R75,D30,R83,U83,L12,D49,R71,U7,L72" "U62,R66,U55,R34,D71,R55,D58,R83"])

(require '[clojure.string :as str])
(require '[clojure.set :as set])

(defn proc [pos dir amt]
  ; (println [pos dir amt])
  (if (= amt 0)
    [#{} pos]
    (let [new-pos (case dir
                    "U" [(- (pos 0) 1) (pos 1)]
                    "D" [(+ (pos 0) 1) (pos 1)]
                    "L" [(pos 0) (- (pos 1) 1)]
                    "R" [(pos 0) (+ (pos 1) 1)])
          [new-poss final-pos] (proc new-pos dir (- amt 1))]
      [(conj new-poss new-pos) final-pos])))

(defn add-pos [poss pos command]
  (let [[dir & amt] (map str (seq command))
        [new-poss new-pos] (proc pos dir (to-int (apply str amt)))]
    [(set/union poss new-poss) new-pos]))

(defn parse-wire [x]
  (reduce (fn [state command] (add-pos (state 0) (state 1) command)) [#{} [0 0]] (str/split x #",")))

(defn abs [x] (if (< x 0) (- x) x))

; (map (comp println parse-wire) lines)
; (println (let [x (vec (map parse-wire lines))] (set/intersection ((x 0) 0) ((x 1) 0))))
(let [x (vec (map parse-wire lines))
      x (set/intersection ((x 0) 0) ((x 1) 0))]
  (apply min (map (fn [x] (+ (abs (x 0)) (abs (x 1)))) x)))
