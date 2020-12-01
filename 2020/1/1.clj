(load-file "../common/common.clj")

(def input (set (map to-int (file-lines "1.txt"))))

(for [x input]
  (let [r (- 2020 x)]
    (if (contains? input r)
      (println "found " x r (* x r)))))
