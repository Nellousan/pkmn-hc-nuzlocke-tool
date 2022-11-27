use crate::common::error::Error;
use crate::common::serializable::Serializable;

/// Trait for items, allows to set/get IDs and quatity of the item.
pub trait Item: Serializable {
    /// Sets the ID of the item to id.
    fn set_id(&mut self, id: i32);

    /// Get the ID of the item.
    fn get_id(&self) -> Result<i32, Error>;

    /// Set the Quantity of the item to Quantity.
    fn set_quantity(&mut self, quantity: i32);

    /// Get the Quantity of the item.
    fn get_quantity(&self) -> Result<i32, Error>;
}
