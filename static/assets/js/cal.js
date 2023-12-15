var item_amounts = {{cart_total_amount}};
var tax = {{tax}}
var packing_cost = {{packing_cost}}
var total = tax + packing_cost;
var coupon_discount = {{coupon.discount}}
console.log(coupon_discount)
if(coupon_discount)
{
    if(item_amounts < 500)
    {
        cal_discount = item_amounts - (item_amounts * coupon_discount / 100) + total + 120
        document.getElementById("total").innerHTML="$" + " " + cal_discount.toFixed()
    }
    else
   {
    cal_discount = item_amounts - (item_amounts * coupon_discount / 100) + total
    document.getElementById("total").innerHTML="$" + " " + cal_discount.toFixed()
    }
}


$(document).ready(function(){
	$('.filter-checkbox').on('click', function(){
		var filter_object={};
		$(".filter-checkbox").each(function(index,ele){
			var filter_value=$(this).val();
			var filter_key=$(this).data('filter');
			console.log(filter_key,filter_value);
			filter_object[filter_key]=Array.from(document.querySelectorAll('input[data-filter='+filter_key+']:checked')).map(function(el){
			 	return el.value;
			});
		});
		$.ajax({
			url:'{% url 'filter-data' %}',
			data:filter_object,
			dataType:'json',
			success:function(res){
				$('#filteredProducts').html(res.data);
			}
		});
	});
});