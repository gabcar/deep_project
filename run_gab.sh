bazel build tensorflow/examples/label_image:label_image && \
bazel-bin/tensorflow/examples/label_image/label_image \
--graph=/tmp/output_graph.pb \
--labels=/tmp/output_labels.txt \
--output_layer=final_result \
--input_layer=Mul \
--image=/Users/gabrielcarrizo/GitHub/deep_project/pre_proc/test_images/0499-image09482.jpg
