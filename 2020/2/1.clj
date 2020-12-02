
(load-file "../common/common.clj")

(require '[clojure.string :as str])

(defn is-valid [c-min c-max c pw]
  (let [num-c (count (filter #(= c %) (map str pw)))]
    (and (<= num-c c-max) (>= num-c c-min))))

(defn parse [line]
  (let [[line pw] (str/split line #": ")
        [line c] (str/split line #" ")
        [c-min c-max] (str/split line #"-")]
    (list (to-int c-min) (to-int c-max) c pw)))


(def input (file-lines "1.txt"))

(count (filter #(= true %) (map (comp #(apply is-valid %) parse) input)))
