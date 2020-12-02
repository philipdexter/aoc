
(load-file "../common/common.clj")

(require '[clojure.string :as str])

(defn -nth [s i]
  (if (< i (count s))
    (nth s i)
    "-"))

(defn is-valid [pos-1 pos-2 c pw]
  (let [pw (map str pw)
        pos-1 (dec pos-1)
        pos-2 (dec pos-2)]
    (or
      (and (= c (-nth pw pos-1)) (not= c (-nth pw pos-2)))
      (and (not= c (-nth pw pos-1)) (= c (-nth pw pos-2))))))

(defn parse [line]
  (let [[line pw] (str/split line #": ")
        [line c] (str/split line #" ")
        [c-min c-max] (str/split line #"-")]
    (list (to-int c-min) (to-int c-max) c pw)))


(def input (file-lines "1.txt"))

(count (filter #(= true %) (map (comp #(apply is-valid %) parse) input)))
