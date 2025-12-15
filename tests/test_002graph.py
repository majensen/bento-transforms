import pytest
from bento_transforms.mdf import TransformReader
from bento_transforms.graph.meta import gtf_to_tf_graph

def test_meta_graph(samplesd):
    tmdf = TransformReader(samplesd / "transforms.yaml",
                           handle='transforms',
                           mdf_schema=samplesd / "mdf-schema-tf.yaml")
    for (hdl, tf) in tmdf.transforms.items():
        assert gtf_to_tf_graph(tf, hdl)
