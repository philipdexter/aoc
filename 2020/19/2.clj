
(load-file "../common/common.clj")

(def rules (vec (get (vec input-split-lines) 0)))
(def input (vec (get (vec input-split-lines) 1)))

(def rules (into {} (map (fn [line] (str/split line #": ")) rules)))
(def rules (assoc rules "8" "42 | 42 8"))
(def rules (assoc rules "11" "42 31 | 42 11 31"))

(def max-depth 5)

(defn string-for-rule [n depth]
  (if (= max-depth depth) ""
    (let [rule (get rules n)]
      (if-let [[_ match] (re-matches #"\"(.*)\"" rule)]
        match
        (let [alts (str/split rule #" \| ")
              alt-strings (map #(map (fn [m] (string-for-rule m (if (= m n) (inc depth) depth))) (str/split % #" ")) alts)]
          (str "(" (str/join "|" (map (partial apply str) (vec (map vec alt-strings)))) ")"))))))

(def pattern (re-pattern (string-for-rule "0" 0)))

(count (filter #(re-matches pattern %) input))
