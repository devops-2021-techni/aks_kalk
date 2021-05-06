provider "azurerm" {
    # The "feature" block is required for AzureRM provider 2.x.
    # If you are using version 1.x, the "features" block is not allowed.
    version = "=2.0.0"
    features {}
}

terraform {
    backend "azurerm" {
    resource_group_name  = "Terraform"
    storage_account_name = "csa1003200138165a03"
    container_name       = "tfstate"
    key                  = "8hiLOU2HXl3AAY5cJVW996kDT0a5bCDSjBbG72U5enEW3a87ZwHZp2Dm4SWbS82Wr+Hg10sW9ZGhQxm6OQ/i2g=="
  }
}

resource "azurerm_resource_group" "rg-hello-azure" {
  name     = "rg-hello-azure"
  location = "francecentral"
}
