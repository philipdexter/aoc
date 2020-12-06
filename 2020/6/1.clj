
(load-file "../common/common.clj")

(reduce + 0 (map (comp count set) (map #(apply str %) input-split-lines)))
