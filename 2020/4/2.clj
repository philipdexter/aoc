
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
                                        (cons (str (str/replace string #"\n" " ") " "(first state)) (rest state)))) '("") input))

(defn has-all-fields [x]
  (every? identity (map #(has-field x %) fields)))

(defn get-field [t field]
  (let [match (re-find (re-pattern (str field ":" "([^ ]+)")) t)]
    (if (> (count match) 1)
      (match 1)
      nil)))


(defn is-valid [x]
  (and
    (has-all-fields x)
    (let [byr (get-field x "byr")] (and
                                     (= 4 (count byr))
                                     (>= (to-int byr) 1920)
                                     (<= (to-int byr) 2002)))
    (let [iyr (get-field x "iyr")] (and
                                     (= 4 (count iyr))
                                     (>= (to-int iyr) 2010)
                                     (<= (to-int iyr) 2020)))
    (let [eyr (get-field x "eyr")] (and
                                     (= 4 (count eyr))
                                     (>= (to-int eyr) 2020)
                                     (<= (to-int eyr) 2030)))
    (let [hgt (get-field x "hgt")
          units (subs hgt (- (count hgt) 2))
          hgt (subs hgt 0 (- (count hgt) 2))] (if (= units "cm")
                                                (and (>= (to-int hgt) 150)
                                                     (<= (to-int hgt) 193))
                                                (and (>= (to-int hgt) 59)
                                                     (<= (to-int hgt) 76))))
    (let [hcl (get-field x "hcl")] (re-find #"#[0-9a-f]{6}" hcl))
    (let [ecl (get-field x "ecl")] (re-find #"amb|blu|rn|gry|grn|hzl|oth" ecl))
    (let [pid (get-field x "pid")] (re-find #"\d{9}" pid))
    ))

(count (filter identity (map is-valid input)))
