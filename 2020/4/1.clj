
(load-file "../common/common.clj")

(def fields '(
              "byr"
              "iyr"
              "eyr"
              "hgt"
              "hcl"
              "ecl"
              "pid"
              ))

(defn has-field [t field] (str/includes? t (str field ":")))

(def input (reduce (fn [state string] (if (empty? string)
                                        (cons "" state)
                                        (cons (str string " "(first state)) (rest state)))) '("") input))

(defn has-all-fields [x]
  (every? identity (map #(has-field x %) fields)))

(count (filter identity (map has-all-fields input)))
