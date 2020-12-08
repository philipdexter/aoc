
(load-file "../common/common.clj")

(defn acc [arg pc acc]
  [(inc pc) (+ acc arg)])
(defn jmp [arg pc acc]
  [(+ pc arg) acc])
(defn nop [arg pc acc]
  [(inc pc) acc])

(defn instruction-for [x]
  (case x
    "acc" acc
    "jmp" jmp
    "nop" nop))

(defn call [op arg pc acc]
  ((instruction-for op) arg pc acc))

(def program
  (vec (map #(let [[op arg] (str/split % #" ")] [op (to-int arg)]) input)))

(loop
  [pc 0
   acc 0
   lines-hit #{}]
  (if (contains? lines-hit pc)
    (println acc)
    (let [lines-hit (conj lines-hit pc)
          [op arg] (program pc)
          [pc acc] ((instruction-for op) arg pc acc)]
      (recur pc acc lines-hit))))
