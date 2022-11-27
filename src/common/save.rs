use crate::common::serializable::Serializable;
use std::error::Error;

pub trait Save: Serializable {}
