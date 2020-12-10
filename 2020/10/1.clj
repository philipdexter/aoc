
(load-file "../common/common.clj")

(def nums (vec (sort (vec (map to-int input)))))

(let [difs (map (fn [i] (- (nums (inc i)) (nums i))) (range (dec (count nums))))]
  (* (+ (apply min nums) (count (filter #(= 1 %) difs))) (inc (count (filter #(= 3 %) difs)))))
