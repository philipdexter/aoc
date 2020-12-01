(load-file "../common/common.clj")

(def input (set (map to-int (file-lines "1.txt"))))

(for [x input]
  (for [y input]
    (let [r (- 2020 x y)]
      (if (contains? input r)
        (println "found " x y r (* x y r))))))
