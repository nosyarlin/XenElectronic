/*
 * XenElectronics Web Store
 * This is a MVP web store for XenElectronics
 *
 * OpenAPI spec version: 0.0.1
 * Contact: rayson.ljk@gmail.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.33
 *
 * Do not edit the class manually.
 *
 */
import {ApiClient} from '../ApiClient';

/**
 * The CheckoutBody model module.
 * @module model/CheckoutBody
 * @version 0.0.1
 */
export class CheckoutBody {
  /**
   * Constructs a new <code>CheckoutBody</code>.
   * @alias module:model/CheckoutBody
   * @class
   */
  constructor() {
  }

  /**
   * Constructs a <code>CheckoutBody</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/CheckoutBody} obj Optional instance to populate.
   * @return {module:model/CheckoutBody} The populated <code>CheckoutBody</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new CheckoutBody();
      if (data.hasOwnProperty('productId'))
        obj.productId = ApiClient.convertToType(data['productId'], 'Number');
      if (data.hasOwnProperty('quantity'))
        obj.quantity = ApiClient.convertToType(data['quantity'], 'Number');
    }
    return obj;
  }
}

/**
 * @member {Number} productId
 */
CheckoutBody.prototype.productId = undefined;

/**
 * @member {Number} quantity
 */
CheckoutBody.prototype.quantity = undefined;

