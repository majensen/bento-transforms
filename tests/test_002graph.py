import pytest
from bento_transforms.mdf import TransformReader
from bento_transforms.graph.meta import gtf_to_tf_graph
from bento_meta.objects import Node, Property
from bento_meta.tf_objects import Transform, TfStep

def test_meta_graph(samplesd):
    meta_tfs = {}
    tmdf = TransformReader(samplesd / "transforms.yaml",
                           handle='transforms',
                           mdf_schema=samplesd / "mdf-schema-tf.yaml")
    
    for (hdl, tf) in tmdf.transforms.items():
        meta_tfs[hdl] = gtf_to_tf_graph(tf, hdl)
        assert meta_tfs[hdl]

    mtf = meta_tfs["fullname_to_fmlnames"]

    assert isinstance(mtf, Transform)
    assert len(mtf.input_props) == 1
    assert len(mtf.output_props) == 3
    assert isinstance(mtf.first_step, TfStep)
    assert isinstance(mtf.last_step, TfStep)

    mstep = mtf.first_step
    assert mstep.entrypoint == "string.split"
    assert mstep.package == "bento-transforms"
    assert mstep.version == "0.1.1"
    assert mstep.params['delimiter'] == " "
