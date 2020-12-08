
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

(defn change-jmps-to-nops [idx]
  (if (= ((program idx) 0) "jmp")
    (assoc program idx ["nop" ((program idx) 1)])))

(defn for-program [program]
  (loop
    [pc 0
     acc 0
     lines-hit #{}]
    (if (= pc (count program))
      acc
      (if (contains? lines-hit pc)
        nil
        (let [lines-hit (conj lines-hit pc)
              [op arg] (program pc)
              [pc acc] ((instruction-for op) arg pc acc)]
          (recur pc acc lines-hit))))))

(filter #(not= nil %) (map for-program (filter #(not= nil %) (map change-jmps-to-nops (range (count program))))))
